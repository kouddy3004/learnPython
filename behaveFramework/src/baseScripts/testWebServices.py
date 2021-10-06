import os

import jsonpath

from behaveFramework.src.reUsables.jsonHandler import JsonHandler
from behaveFramework.src.testWebService.apiHandler import ApiHandler


class TestWebServices:
    projectPath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    envDetails={}
    api = ApiHandler.getInstance()

    @staticmethod
    def getInstance():
        return TestWebServices()

    def setEnvDetails(self,envName):
        envPath=self.projectPath+"\\src\\testWebService\\reqDetails\\env.json"
        self.envDetails=JsonHandler.getInstance().readjson(envPath).get(envName.lower())

    def validateGetRequest(self):
        response=self.api.getRequest(self.envDetails.get("baseUrl")+self.envDetails.get("getUrl"))
        print(response)
        print(jsonpath.jsonpath(response,"data[2].email")[0])

    def validateDeleteRequest(self):
        statusCode=self.api.deleteRequest(self.envDetails.get("baseUrl")+self.envDetails.get("deleteUrl"))
        print("Deleted and the status code is "+str(statusCode))



