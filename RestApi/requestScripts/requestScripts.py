import os

from commonScripts.jsonHandler import JsonHandler
import requests

class RequestScript():
    envDetail={}
    currentPath = os.path.dirname(os.path.abspath(__file__))
    restPath = os.path.dirname(currentPath)

    def __init__(self,envName):
        json=JsonHandler()
        self.envDetail=json.readjson(self.restPath+"\\jsonFiles\\env.json")[envName]

    def getRequest(self,parameters):
        if(self.envDetail['getUrl'][0]!="/"):
            self.envDetail['getUrl']="/"+self.envDetail['getUrl']
        getUrl=self.envDetail['baseUrl']+self.envDetail['getUrl']
        print("HTTP  Get URL : " +getUrl)
        return requests.get(getUrl,params=parameters)
