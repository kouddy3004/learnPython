from behave import *


@given("Login with UserName and Password")
def loginAcmeAPP(context):
    print("Login Method")


@when("Fetch values from UI")
def fetchFromUI(context):
    print("Do for values From UI")


@when("Fetch values from Database")
def fetchFromDB(context):
    print("Do for values From DB")


@then("Validate values from UI and Database")
def validateUIandDB(context):
    print("Do for UI and DB validation")