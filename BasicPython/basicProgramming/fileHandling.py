import os

filePath=os.path.dirname(os.path.abspath(__file__))+"\\files\\"
filename="sample.txt"

def readFile():
    try:
        with open(filePath+filename,mode='r+') as file:
            contents=[ i for i in file.readlines() if i!="\n"]
            return contents
    except Exception as e:
        if(e.__class__.__name__=="FileNotFoundError"):
            print(e)
        else:
            print(e.__class__.__name__)

def writeFile():
    contents=["Writing the file\n"]
    for i in readFile():
        contents.append(i)
    contents.append("\nFiles Wrote")
    print(contents)
    if contents is not None:
        with open(filePath+"writingFilefromPython",mode="w+") as file:
            file.writelines(contents)

writeFile()