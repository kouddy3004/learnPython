print("List Comprehension")
windowsList = [i for i in range(1, 30) if i == 1 or i % 6 == 0 or i % 6 == 1]
print(windowsList)
print("")

print("Get unique and duplicate value")
allList=['Koushik','Subramanian','Koushik','Subramanian','Kou']
print(allList)
uniqueList=[uni for uni in set(allList)]
print(uniqueList)
duplicateList=[dupe for pos,dupe in enumerate(allList) if dupe in allList[:pos]]
print(duplicateList)
print("")

print("Concatenation")
concatenateString = " ".join(["Koushik", "Subramanian"])
print(concatenateString)
