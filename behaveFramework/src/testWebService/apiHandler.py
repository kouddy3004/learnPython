import json

import jsonpath
import requests


class ApiHandler:
    @staticmethod
    def getInstance():
        return ApiHandler()

    def getRequest(self,url):
        response=requests.get(url)
        jsonResponse=json.loads(response.text)
        return jsonResponse

    def deleteRequest(self,url):
        response=requests.delete(url)
        return response.status_code




