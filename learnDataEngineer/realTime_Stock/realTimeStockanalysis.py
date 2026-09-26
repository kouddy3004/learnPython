import pandas as pd
import yfinance as yf


def myHoldings():
    df = pd.read_excel("Holdings_20-Sep-2026_16.00.57.xlsx")
    totalInvestedDf = df.iloc[:1, :4].copy()
    print(totalInvestedDf)

    perHoldingDf = df.iloc[3:].copy()
    perHoldingDf.columns = df.iloc[2]
    perHoldingDf.columns.name = None
    return perHoldingDf


def getTodayStatus(df):
    holdingList = [x + ".NS" for x in df[df["Invested"] != "--"]["Symbol (20)"].tolist()]
    tickerDf = yf.download(holdingList, period="5d", interval="1d")
    print(tickerDf)


myHoldingDf = myHoldings()
getTodayStatus(myHoldingDf)
