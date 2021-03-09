import os

from RestApi.requestScripts.requestScripts import RequestScript
currentPath=os.path.dirname(os.path.abspath(__file__))
projectPath = os.path.dirname(currentPath)

def getRequest():
    request = RequestScript("reqRes")
    response = request.getRequest()
    if response.status_code==200:
        print(response.status_code)
        print(response.headers)
        print(response.json()['data'])
    else:
        print("HTTP not recognised "+str(response.status_code))


getRequest()
