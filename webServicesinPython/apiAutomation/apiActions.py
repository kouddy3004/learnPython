import requests

class ApiActions:
   #Get Request from Rest
    def getRequest(self,url):
        response = requests.get(url).json()
        return response

   # Get Response for Posted Request
    def postRequest(self,url,data):
        response=requests.post(url,data).json()
        return response

obj=ApiActions()
req=obj.getRequest("https://reqres.in/api/users?delay=3")
print("Request Json : "+str(req))
response = obj.postRequest("https://reqres.in/api/users",req)
print("Response JSon : "+str(response))
print("Extracting creation date from response json : "+response['createdAt'])