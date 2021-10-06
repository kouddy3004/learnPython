import os, sys
from jproperties import Properties


class PropertyHandler:
    projectPath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    config=None
    def __init__(self):
        self.config = Properties()
        with open("{0}\\resources\\env.properties".format(str(self.projectPath)), 'rb') as readProps:
            self.config.load(readProps)

    @staticmethod
    def getInstance():
        return PropertyHandler()

    def readProperty(self, fileKey):
            filePath="{0}{1}".format(self.projectPath,self.config.get(fileKey).data)
            return filePath

    def readProperties(self):
        return self.config

