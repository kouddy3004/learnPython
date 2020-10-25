import os
from commonScripts.jsonHandler import JsonHandler

currentPath=os.path.dirname(os.path.abspath(__file__))
projectPath = os.path.dirname(currentPath)

class Test():
    def checkJsonRead(self):
        json=JsonHandler()
        sampleJson=json.readjson(currentPath+"\\jsonFiles\\sample.json")
        for q1,value in sampleJson['quiz']['maths']['q2'].items():
            print(q1+" : "+str(value))

obj=Test()
obj.checkJsonRead()