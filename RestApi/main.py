import os

from RestApi.requestScripts.requestScripts import RequestScript
currentPath=os.path.dirname(os.path.abspath(__file__))
projectPath = os.path.dirname(currentPath)

def getRequest():
    request = RequestScript("reqRes")
    response = request.getRequest({'id': 8})
    print(response.json()['data'])
    print(response.status_code)
    print(response.headers)

getRequest()
