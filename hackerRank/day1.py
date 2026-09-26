def countResponseTimeRegressions():
    responseTimes = [100, 200, 150, 300]
    count = 0
    for i in range(1, len(responseTimes) + 1):
        avg = 0
        for j in range(i):
            avg += responseTimes[j]
            if j == i - 1:
                avg = int(avg / (j + 1))
                if avg < responseTimes[i - 1]:
                    count += 1


def findSmallestMissingPositive():
    orderNumbers = [3, 4, -1, 1]
    ans = 1
    while ans in orderNumbers:
        ans += 1
    print(ans)


def isAlphabeticPalindrome():
    code = "A1b2B!a"
    code = "".join(char.lower() for char in code if char.isalpha())
    if code == code[::-1]:
        return True
    return False


def mergeAlternately():
    word1, word2, word3 = "ab", "pqrs", ""
    max = len(word2) if len(word2) > len(word1) else len(word1)
    for i in range(max):
        if i < len(word1):
            word3 += word1[i]
        if i < len(word2):
            word3 += word2[i]
    print(word3)


def gcdOfStrings() -> str:
    str1, str2 = "A", "ABC"
    op = str1 if len(str1) > len(str2) else (str2 if len(str2) > len(str1) else "")
    print(op)


def kidsWithCandies():
    candies, extraCandies = [4, 2, 1, 1, 2], 1
    max_Count = sorted(candies)[-1]
    result = [True if candies[i] + extraCandies >= max_Count else False for i in range(len(candies))]
    print(result)


def reverseVowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = "IceCreAmsA"
    a = [x for x in s]
    result = ""
    vowindex = [ind for ind in range(len(s)) if s[ind].lower() in vowels]
    while len(vowindex) > 1:
        print(vowindex)
        a[vowindex[0]], a[vowindex[-1]] = a[vowindex[-1]], a[vowindex[0]]
        vowindex.pop(0)
        vowindex.pop(-1)
    for x in a:
        result += x
    print(result)


def reverseWord():
    s = "  hello world  ".strip()
    li = s.split(" ")
    re = ""
    for i in reversed(li):
        re += " " + i
    print(re.strip())


def moveZeroes():
    nums = [0, 1, 0, 3, 12]
    print(nums)


if __name__ == "__main__":
    moveZeroes()
