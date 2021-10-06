import json

class JsonHandler():
    @staticmethod
    def getInstance():
        return JsonHandler()

    def readjson(self,path):
        with open(path) as file:
            jsonDict=json.load(file)
        return jsonDict