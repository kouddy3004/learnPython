from behaveFramework.src.baseScripts.baseClass import BaseClass


class runAcmeApp(BaseClass):
    def __init__(self):
        super().__init__()
        print("From ACME")


obj = runAcmeApp()
