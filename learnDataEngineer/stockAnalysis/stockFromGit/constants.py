import datetime


class Constants():

    def __init__(self, inAws=True):
        self.__dt = datetime.datetime.now()
        monthStr = self.__dt.strftime("%d %B, %Y")
        COMPONENT_NAME = 'STOCK_DATA_EXTRACT'

        ERROR_MSG = f'NEED ATTENTION **API ERROR KEY EXPIRED * ON {monthStr} **'
        SUCCESS_MSG = f'SUCCESSFULLY EXTRACTED FILES FOR {monthStr}*'

        SUCCESS_DESCRIPTION = 'Success'

        ENVIRONMENT = 'dev'
        NOTIFICATIONARN = None
        BUCKET_NAME = None
        BUCKET_Prefix = None
        self.URL_API = 'https://api.github.com/repos/squareshift/stock_analysis/contents/'

        if inAws:
            # Global AWS clients
            import boto3
            self.__ssm = boto3.client("ssm", region_name="us-east-1")
            self.__sns = boto3.client("sns", region_name="us-east-1")
            self.__s3 = boto3.client("s3")

            self.__NOTIFICATIONARN = '/data/stockProjectFromGit/mailnotification'

            self.__BUCKET_NAME = '/data/s3-stock-bucket-name'
            self.__BUCKET_Prefix = 'stock-fromgit-reports/'

    def getEnv(self):
        return self.URL_API

    def getBucketDetails(self):
        bucketName = self.__ssm.get_parameter(
            Name=self.__BUCKET_NAME,
            WithDecryption=True
        )["Parameter"]["Value"]
        bucketPrefix = self.__BUCKET_Prefix
        return bucketName, bucketPrefix

    def getEmailContent(self, status: bool):
        sns_arn = self.__ssm.get_parameter(Name=self.__NOTIFICATIONARN, WithDecryption=True)["Parameter"]["Value"]

        if status:
            subject = "?Stock Pipeline for getting Stock from Git Repo - Success"
            message = (
                "? STOCK PIPELINE - Successfully extracted on the below S3\n"
                "============================\n"
                "Bucket      : {0}\n"
                "File        : {1}\n"
                "Rows        : {2}\n"
                f"Timestamp   : {self.__dt.strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
        else:
            subject = "?Stock Pipeline for getting Stock from Git Repo - Failure"
            message = (
                "? STOCK PIPELINE - FAILED because of the below reason\n"
                "===========================\n"
                "Error       : {0}\n"
                f"Timestamp   : {self.__dt.strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
        return self.__sns, sns_arn, subject, message
