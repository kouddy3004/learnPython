from behaveFramework.src.reUsables.propertyHandler import PropertyHandler
from behaveFramework.src.reUsables.pandaHandler import PandaHandler
import os

projectPath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

properties=PropertyHandler.getInstance().readProperties()
xmlFilePath=projectPath+properties.get("xmlFiles").data
csvFilePath=projectPath+properties.get("csvFiles").data

xmlDF=PandaHandler.getInstance().readXml(xmlFilePath+"\\Samplexml200.xml","./feeds")
xmlDF.iloc[0:2].to_csv(csvFilePath+"\\Samplexml200.csv",index=False)
csvDF=PandaHandler.getInstance().readCsv(csvFilePath+"\\Samplexml200.csv")
ids=["{0}".format(idx) for idx in xmlDF['id'].values]
xmlIntersectsCsv=(csvDF.loc[xmlDF.id.isin(ids)])
for index, row in xmlIntersectsCsv.iterrows():
    print(str(row['id'])+" created at "+row['createdAt'])


