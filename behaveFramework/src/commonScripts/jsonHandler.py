import json

class JsonHandler():
    def readjson(self,path):
        with open(path) as file:
            jsonDict=json.load(file)
        return jsonDict