import datetime as dt
import json
import logging
import sys
import time

import pandas as pd
import requests
from jsonpath_ng import parse


# ---------------------------------------------------------------------------
# Structured JSON logging setup (CloudWatch-optimized)
# ---------------------------------------------------------------------------
# Schema (one JSON object per line, printed to stdout):
#   timestamp : ISO 8601 UTC, millisecond precision, "...Z"
#   level     : "INFO" | "WARN" | "ERROR" | "DEBUG"
#   message   : static, human-readable, starts with an active verb, NO variables
#   context   : all dynamic ids/metadata/variables go here
#
# Rule: never interpolate variables into `message`. Always pass them as
# keyword args to log_info/log_error/log_debug/log_warn -> they land in `context`.


class JsonFormatter(logging.Formatter):
    """
    Plain-text, single-line format for CloudWatch:

        TIMESTAMP LEVEL [method] Static message key1=value1 key2=value2 ...

    - Everything is plain text: no braces, no quotes, no JSON.
    - Still one line per event, so it tails cleanly in CloudWatch.
    - Values with spaces are wrapped in double quotes so key=value pairs
      stay unambiguous; values are otherwise printed as-is.
    - Still greppable/queryable in CloudWatch Insights via
      `parse @message "*=*"` or simple `filter @message like /key=value/`.
    """
    LEVEL_MAP = {"WARNING": "WARN"}

    @staticmethod
    def _format_value(value) -> str:
        text = str(value)
        if " " in text or "\n" in text or '"' in text:
            text = text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
            return f'"{text}"'
        return text

    def format(self, record: logging.LogRecord) -> str:
        record_dt = dt.datetime.utcfromtimestamp(record.created)
        timestamp = record_dt.strftime("%Y-%m-%dT%H:%M:%S.") + f"{int(record.msecs):03d}Z"
        level = self.LEVEL_MAP.get(record.levelname, record.levelname)

        context = dict(getattr(record, "context", {}) or {})
        method = context.pop("method", None)

        if record.exc_info:
            context["stack_trace"] = self.formatException(record.exc_info)

        line = f"{timestamp} {level:<5}"
        if method:
            line += f" [{method}]"
        line += f" {record.getMessage()}"

        if context:
            pairs = " ".join(f"{k}={self._format_value(v)}" for k, v in context.items())
            line += f" {pairs}"

        return line


def _build_logger() -> logging.Logger:
    _logger = logging.getLogger("stock_pipeline")
    _logger.setLevel(logging.INFO)  # set to logging.DEBUG locally for verbose tracing
    _logger.propagate = False

    if not _logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JsonFormatter())
        _logger.addHandler(handler)

    return _logger


logger = _build_logger()


def log_info(message: str, **context) -> None:
    logger.info(message, extra={"context": context})


def log_warn(message: str, **context) -> None:
    logger.warning(message, extra={"context": context})


def log_debug(message: str, **context) -> None:
    logger.debug(message, extra={"context": context})


def log_error(message: str, exc: Exception = None, **context) -> None:
    if exc is not None:
        context.setdefault("error_summary", str(exc))
    logger.error(message, extra={"context": context}, exc_info=exc is not None)


# ---------------------------------------------------------------------------
# S3 configuration - update these to match your setup
# ---------------------------------------------------------------------------
timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"stock_data_{timestamp}.csv"


def getValueByJsonPath(jsonVal, jsonPath):
    path_expression = parse(jsonPath)
    matches = path_expression.find(jsonVal)
    log_debug("Evaluated JSONPath expression", method="getValueByJsonPath",
              json_path=jsonPath, match_count=len(matches))
    # .value retrieves the extracted data
    return matches


def readCsv(csvPath):
    t0 = time.perf_counter()
    df = pd.read_csv(csvPath)
    duration_ms = round((time.perf_counter() - t0) * 1000, 2)
    log_debug("Loaded CSV into DataFrame", method="readCsv", source=csvPath,
              rows=df.shape[0], columns=df.shape[1], duration_ms=duration_ms)
    return df


def __getUrls(stockApi):
    log_info("Requesting stock API", method="__getUrls", stock_api=stockApi)
    t0 = time.perf_counter()
    stockResponse = requests.get(stockApi)
    duration_ms = round((time.perf_counter() - t0) * 1000, 2)

    if stockResponse.status_code == 200:
        log_info("Stock API authenticated successfully", method="__getUrls",
                 status_code=stockResponse.status_code, duration_ms=duration_ms)
        stockResp = stockResponse.json()
        downloadUrls = getValueByJsonPath(stockResp, "$[*].download_url")
        log_info("Extracted download URLs from stock API response", method="__getUrls",
                 url_count=len(downloadUrls))
        return downloadUrls
    else:
        log_error("Stock API authentication failed", method="__getUrls",
                  error_code="stock_api_auth_failed",
                  status_code=stockResponse.status_code,
                  duration_ms=duration_ms,
                  response_body=stockResponse.text)


def __readCsv(url):
    t0 = time.perf_counter()
    df = readCsv(url)
    duration_ms = round((time.perf_counter() - t0) * 1000, 2)
    log_debug("Fetched CSV file", method="__readCsv", url=url,
              row_count=len(df), duration_ms=duration_ms)
    return df


def __getStockFromGitRepo(stockApi):
    log_info("Started stock data collection from git repo", method="__getStockFromGitRepo")
    stage_t0 = time.perf_counter()

    urls = __getUrls(stockApi)
    dataList = []
    metaData = None

    if urls:
        download_t0 = time.perf_counter()
        for i, url in enumerate(urls, start=1):
            item_t0 = time.perf_counter()
            df = __readCsv(url.value)
            fileName = url.value.split("/")[-1].replace(".csv", "")
            item_duration_ms = round((time.perf_counter() - item_t0) * 1000, 2)
            log_info(f"Fetching Data from {url.value}", method="__getStockFromGitRepo")
            if fileName == 'symbol_metadata':
                metaData = df
                log_debug("Identified metadata file", method="__getStockFromGitRepo",
                          file_index=i, total_files=len(urls), file_name=fileName,
                          duration_ms=item_duration_ms)
                log_info(f"Identified metadata file {str(len(metaData))}", method="__getStockFromGitRepo")
            else:
                df["Symbol"] = fileName
                dataList.append(df)
                log_debug("Tagged symbol DataFrame", method="__getStockFromGitRepo",
                          file_index=i, total_files=len(urls), symbol=fileName,
                          row_count=len(df), duration_ms=item_duration_ms)
                log_info(f"Tagged {str(len(df))} Data of {str(fileName)}", method="__getStockFromGitRepo")

        download_duration_ms = round((time.perf_counter() - download_t0) * 1000, 2)
        log_info("Downloaded and parsed all stock files includes Filename", method="__getStockFromGitRepo",
                 file_count=len(urls), duration_ms=download_duration_ms)
    else:
        log_error("No download URLs returned from stock API", method="__getStockFromGitRepo",
                  error_code="no_download_urls")

    if dataList:
        merge_t0 = time.perf_counter()
        dfs = pd.concat(dataList, ignore_index=True)
        log_info("Concatenated symbol DataFrames", method="__getStockFromGitRepo",
                 frame_count=len(dataList), row_count=dfs.shape[0], column_count=dfs.shape[1])

        if metaData is None:
            log_error("Symbol metadata file missing; merge will produce empty Sector columns",
                      method="__getStockFromGitRepo", error_code="metadata_missing")

        dfs_Metadata = pd.merge(dfs, metaData, on="Symbol", how="left")
        merge_duration_ms = round((time.perf_counter() - merge_t0) * 1000, 2)
        log_info("Merged stock data with symbol metadata", method="__getStockFromGitRepo",
                 row_count=dfs_Metadata.shape[0], column_count=dfs_Metadata.shape[1],
                 duration_ms=merge_duration_ms)

        agg_t0 = time.perf_counter()
        resultant_df = dfs_Metadata.groupby("Sector").agg(
            {"open": "mean", "high": "max", "low": "min", "close": "mean"}).reset_index()  # Sector related data
        agg_duration_ms = round((time.perf_counter() - agg_t0) * 1000, 2)
        log_info("Aggregated stock data by sector", method="__getStockFromGitRepo",
                 sector_count=resultant_df.shape[0], duration_ms=agg_duration_ms)

        total_duration_ms = round((time.perf_counter() - stage_t0) * 1000, 2)
        log_info("Completed stock data collection from git repo", method="__getStockFromGitRepo",
                 duration_ms=total_duration_ms)
        return resultant_df
    else:
        total_duration_ms = round((time.perf_counter() - stage_t0) * 1000, 2)
        log_error("No symbol data collected; skipping merge and aggregation",
                  method="__getStockFromGitRepo", error_code="empty_data_list",
                  duration_ms=total_duration_ms)


def uploadToS3(local_file, bucket_name, s3_key):
    """
    Uploads a local file to the specified S3 bucket/key.
    """
    log_info("Uploading result to S3", method="uploadToS3", bucket=bucket_name, key=s3_key)
    t0 = time.perf_counter()
    try:
        import boto3
        s3_client = boto3.client("s3")
        s3_client.put_object(Bucket=bucket_name, Key=s3_key, Body=local_file)
        duration_ms = round((time.perf_counter() - t0) * 1000, 2)
        log_info("Uploaded result to S3 successfully", method="uploadToS3",
                 bucket=bucket_name, key=s3_key, duration_ms=duration_ms)
    except Exception as e:
        duration_ms = round((time.perf_counter() - t0) * 1000, 2)
        log_error("Failed to upload result to S3", exc=e, method="uploadToS3",
                  error_code="s3_upload_failed", bucket=bucket_name, key=s3_key,
                  duration_ms=duration_ms)
        raise


def __getSectorList(resultant_df, sector_list, obj, inAWS=True):
    log_info("Filtering result to target sectors", method="__getSectorList",
             sectors=sector_list)
    resultant_df = resultant_df[resultant_df["Sector"].isin(sector_list)].reset_index(drop=True)
    log_debug("Filtered DataFrame preview", method="__getSectorList",
              preview=resultant_df.to_dict(orient="records"))
    log_info("Filtered sector data", method="__getSectorList", row_count=len(resultant_df))

    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    local_file_name = f"stock_data_{timestamp}.csv"

    if inAWS:
        csvData = resultant_df.to_csv(index=False)
        S3_BUCKET_NAME, S3_KEY_PREFIX = obj.getBucketDetails()
        s3_key = f"{S3_KEY_PREFIX}{local_file_name}" if S3_KEY_PREFIX else local_file_name
        log_info("Resolved S3 destination", method="__getSectorList",
                 bucket=S3_BUCKET_NAME, key=s3_key)
        uploadToS3(csvData, S3_BUCKET_NAME, s3_key)
        log_info("Completed sector extraction with S3 upload", method="__getSectorList",
                 bucket=S3_BUCKET_NAME, key=s3_key, row_count=len(resultant_df))
        return {"bucket": S3_BUCKET_NAME, "key": s3_key, "rows": len(resultant_df)}
    else:
        resultant_df.to_csv(local_file_name, index=False)
        log_info("Completed sector extraction with local file write", method="__getSectorList",
                 local_file=local_file_name, row_count=len(resultant_df))
        return {"local_file": local_file_name, "rows": len(resultant_df)}


def sendSnsEmail(const, status, result):
    """
    Publishes a message to the SNS topic (SNS_TOPIC_ARN env var) which
    fans out to any subscribed email addresses.
    """
    log_info("Preparing SNS notification", method="sendSnsEmail", status=status)
    sns_client, topic_arn, subject, message = const.getEmailContent(status)
    if status:
        message = message.format(result["bucket"], result["key"], str(result["rows"]))
    else:
        message = message.format(str(result))

    if not topic_arn:
        log_error("SNS topic ARN not configured; notification skipped",
                  method="sendSnsEmail", error_code="sns_topic_arn_missing")
        return

    try:
        import boto3
        # Subject has a 100-char limit enforced by SNS
        sns_client.publish(TopicArn=topic_arn, Subject=subject[:100], Message=message)
        log_info("Published SNS notification successfully", method="sendSnsEmail",
                 topic_arn=topic_arn, status=status)
    except Exception as e:
        log_error("Failed to publish SNS notification", exc=e, method="sendSnsEmail",
                  error_code="sns_publish_failed", topic_arn=topic_arn)


def getStocksFromRepoAndExtractSectorResult(const, inAWS=True):
    pipeline_t0 = time.perf_counter()
    log_info("Started pipeline execution", method="getStocksFromRepoAndExtractSectorResult")

    stockApi = const.getEnv()
    log_info("Resolved stock API endpoint", method="getStocksFromRepoAndExtractSectorResult",
             stock_api=stockApi)

    df = __getStockFromGitRepo(stockApi)
    if df is None:
        log_error("Stock data collection returned no data; sector extraction cannot proceed",
                  method="getStocksFromRepoAndExtractSectorResult",
                  error_code="stock_collection_empty")

    sector_list = ["ENERGY & TRANSPORTATION", "LIFE SCIENCES"]
    log_info("Extracting target sector data", method="getStocksFromRepoAndExtractSectorResult",
             sectors=sector_list)

    result = __getSectorList(df, sector_list, const, inAWS)

    total_duration_ms = round((time.perf_counter() - pipeline_t0) * 1000, 2)
    log_info("Completed pipeline execution", method="getStocksFromRepoAndExtractSectorResult",
             duration_ms=total_duration_ms, result=result)
    return result
