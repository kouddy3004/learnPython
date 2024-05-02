def findTriplets(a):
    count = 0
    for i in range(len(a)):
        for j in range(i + 1):
            if a[i] + a[j] in a and i != j:
                count += 1
    print(count)


def maxSubArraySum(arr, N):
    i = 1
    max = arr[0]
    while (i < N):
        max += arr[i]
        i += 1
    if max < 0:
        max = arr[0]
        i = 1
        while (i < N):
            if max < arr[i]:
                max = arr[i]
            i += 1
    print(max)


def missingNumber(array, n):
    i = 1
    missNum = 0
    while (i < max(array)):
        if i not in array:
            missNum = i
        i += 1
    print(missNum)


def sortedArray(arr1, arr2, n, m):
    arr1 = sorted(arr1 + arr2)
    arr2 = arr1[n:len(arr1)]
    arr1 = arr1[:n]
    print(arr1, arr2)


def reArrange(arr, n):
    sortArr = sorted(arr, reverse=True)
    reArr = [max(sortArr), min(sortArr)]
    while (len(sortArr) > 1):
        sortArr.remove(max(sortArr))
        sortArr.remove(min(sortArr))
        reArr.append(max(sortArr))
        if max(sortArr) != min(sortArr):
            reArr.append(min(sortArr))
    print(reArr)


# findTriplets([1, 5, 3, 2])
# findTriplets([2,3,4])
# maxSubArraySum([1, 2, 3, -2, 5], 5)
# maxSubArraySum([-1, -2, -3, -4], 4)
# maxSubArraySum([-10, -2, -3, -4], 4)
# missingNumber([1, 2, 3, 41], 41)
# sortedArray([1, 3, 5, 7], [0, 2, 6, 8, 9], 4, 5)
# reArrange([1, 2, 3, 4, 5, 6], 6)
# reArrange([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110], 11)
