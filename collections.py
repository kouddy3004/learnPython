#List
print("LIST")
print(" -- ")
names=["KOushik","Subramanian"]
nums=[1,2,3]
misc=[]
print(misc)
misc.extend(names)
print(misc)
misc.extend(nums)
print(misc)

#Set and Tuples
print("\nSet and Tuples")
print(" ----------- ")
tup=(12,22,11,44,12)
set={12,33,33,11,11,43,12}
print(set)
print(set.union(tup))