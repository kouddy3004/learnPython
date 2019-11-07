import pandas as pd
from fileHandler import FileHandler
import json

class ReadFiles:
    #Reading specific TestCases from Test Case excel
    def readTestCase(self,testCase="TC01"):
        excelFilePath = FileHandler.setProjectPath() + "\\databank\\testCase\\TestCase.xlsx"
        data= pd.read_excel(excelFilePath)
        dictData={}
        for i in data.index:
            if(data['TCName'][i]==testCase):
                dictData=data.iloc[i]
        return dictData

    # Reading ALL the TestCases from Test Case excel
    def readTestCases(self):
        excelFilePath = FileHandler.setProjectPath() + "\\databank\\testCase\\TestCase.xlsx"
        data= pd.read_excel(excelFilePath)
        return data

    # Reading Json Files
    def readJson(self,jsonFile="TC01.json"):
        jsonData={}
        jsonFile = FileHandler.setProjectPath() + "\\dataBank\\json\\"+jsonFile
        with open(jsonFile) as readJson:
            jsonData = json.load(readJson)
        return jsonData

obj=ReadFiles()
print(obj.readTestCase())