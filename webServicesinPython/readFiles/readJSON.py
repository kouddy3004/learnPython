import json
from fileHandler import FileHandler
class ReadJson:

    def readJson(self,jsonFile="TC01.json"):
        jsonData={}
        jsonFile = FileHandler.setProjectPath() + "\\dataBank\\json\\"+jsonFile
        with open(jsonFile) as readJson:
            jsonData = json.load(readJson)

        return jsonData

