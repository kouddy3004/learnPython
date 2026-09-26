import pandas as pd


def readCsv(csvPath):
    df = pd.read_csv(csvPath)
    return df