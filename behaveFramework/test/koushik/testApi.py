from behaveFramework.src.baseScripts.testWebServices import TestWebServices

#test ReqRes
def testReqRes():
    test=TestWebServices.getInstance()
    test.setEnvDetails("reqres")
    test.validateGetRequest()
    test.validateDeleteRequest()


testReqRes()