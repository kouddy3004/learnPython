import copy

class ArraySets():

    def findTriplets(self,inputArray):
        print("Find Triplets")
        print("Input "+str(inputArray))
        list=[]
        for i in range(len(inputArray)):
            a=inputArray[i]
            for j in inputArray:
                if a is not j:
                    b=a+j
                    if b in inputArray:
                        list.append(str(min(j,a))+"+"+str(max(j,a))+"="+str(b))
        setOf=set(list)
        print(len(setOf))
        if(len(setOf)>0):
            for i in setOf:
                print(i)

    def missingArray(self,inputArray):
        print("Find Missing Number")
        print(inputArray)
        missingNumbers=[miss for miss in range(1,max(inputArray)) if miss not in inputArray]
        print(missingNumbers)

    def mergeTwoSortArray(self,a1,a2):
        print("Sort 2 Arrays and merge")
        print("Array 1 "+str(a1))
        print("Array 2 " + str(a2))
        a1.extend(a2)
        a1.sort()
        print(a1)

    def reArrangeArray(self,inputArray):
        print("Re-Arrange Array")
        print(inputArray)
        reArrangeArray=[]
        temp=copy.deepcopy(inputArray)
        for i in range(1,len(temp)+1):
            if(i%2!=0):
                reArrangeArray.append(max(temp))
                temp.remove(max(temp))
            else:
                reArrangeArray.append(min(temp))
                temp.remove(min(temp))

        print(reArrangeArray)







