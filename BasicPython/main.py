from BasicPython.basicProgramming.sdeSet.arraysSet import ArraySets
from BasicPython.basicProgramming.sdeSet.backTrackSet import BackTrackSet
from BasicPython.basicProgramming.sdeSet.genericSet import GenericSet
from BasicPython.basicProgramming.sdeSet.stringSet import StringSet


def genericCompletedSet():
    generic = GenericSet()
    generic.fibonacciSeries(9)

def completedArraySet():
    array=ArraySets()
    array.findTriplets([2,3,4,5])
    array.missingArray([1, 10])
    array.mergeTwoSortArray([1, 3, 5, 7], [0, 2, 6, 8, 9])
    array.reArrangeArray([10, 20, 30, 40, 50, 60, 90, 70, 110, 80, 100, 90])

def completedStringSet():
    string = StringSet()
    string.reverseWords("I am Koushik"," ")
    string.removeDuplicate("GeeksforgeekS")
    string.aTOi("123a")
    string.srStr("GeeksForGeeks", "Fr")

bc=BackTrackSet()
bc.generateIp("255000255")





