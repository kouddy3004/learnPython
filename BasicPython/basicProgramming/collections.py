# List
print("LIST")
print(" -- ")
names = ["KOushik", "Subramanian"]
nums = [1, 2, 3]
misc = []
print(misc)
misc.extend(names)
print(misc)
misc.extend(nums)
print(misc)

# sets and Tuples
print("\nsets and Tuples")
print(" ----------- ")
tup = (12, 22, 11, 44, 12)
print(tup)
sets = {12, 33, 33, 11, 11, 43, 12}
print(sets)
sets = sets.union(tup)
print(sorted(sets))

# Dictionary
print("\nDictionary")
print(" ------- ")

dicti = dict(zip(sorted(sets), misc))
for key in dicti.keys():
    print(str(key) + " : " + str(dicti.get(key)))
