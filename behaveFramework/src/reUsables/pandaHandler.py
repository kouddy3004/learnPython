import xml.etree.ElementTree as et

import pandas as pd


class PandaHandler:

    @staticmethod
    def getInstance():
        return PandaHandler()

    def tranform_xml(self, xmlroot, findBy):
        xmlList = []
        for xml in xmlroot.findall(findBy):
            xmlDict = {}
            for value in xml:
                xmlDict[value.tag] = value.text
            xmlList.append(xmlDict)
        return xmlList

    def readXml(self, filePath, findBy="/feeds"):
        xmlDF = pd.DataFrame(self.tranform_xml(et.parse(filePath).getroot(), findBy))
        return xmlDF

    def readCsv(self,filePath):
        return pd.read_csv(filePath,index_col=False)

