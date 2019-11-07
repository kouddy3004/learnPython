import os

class FileHandler:
    @staticmethod
    def setProjectPath():
        return os.path.dirname(__file__)