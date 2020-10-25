

class StringSet:

    def reverseWords(self,string,splitParam=None):
        if splitParam is None:
            print(string[::-1])
        else:
            list=string.split(splitParam)
            print(list[::-1])

    def removeDuplicate(self,string):
        temp=""
        for i in range(len(string)):
            count=1
            for j in range(len(string)):
                if (string[i].upper()==string[j].upper() and i!=j and j<i):
                   count=count+1
            if(count==1):
                temp=temp+string[i]
        print(temp)

    def aTOi(self,string):
        if(string.isalpha()):
            for i in range(len(string)):
                print("The Ascii Character of "+string[i]+" is "+str(ord(string[i])))
        elif(string.isdecimal()):
            print(string)
        else:
            print(-1)

    def srStr(self,string,findString):
        pos=-1
        if findString.upper() in string.upper():
            for i in range(len(string)):
                if findString[0].upper() in string[i].upper():
                    pos=i
                    break
        print(pos)







