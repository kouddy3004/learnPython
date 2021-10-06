from behave import *


@given("Open {searchEngine} in {browser}")
def openBrowser(context, searchEngine, browser):
    print("{0} has been opened in the browser {1}".format(searchEngine, browser))


@then("search for {keyWord}")
def searchKeyWord(context, keyWord):
    print("Searching for {0}".format(keyWord))
