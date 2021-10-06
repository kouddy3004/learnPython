#Find Occurance in a string
def findOccurance(S):
    # write your code in Python 3.6
    occurance=""
    for i in range(len(S)):
        for j in range(len(S)):
            if(i!=j and S[i]==S[j]):
                occurance=S[i]
    print(occurance)
#digit sum to N
def sumOfDigits(N):
    sumOfDigit=0
    while (N!=0):
        sumOfDigit=sumOfDigit+(N%10)
        N=N//10
    print(sumOfDigit)



def debugVonage(N):
    enable_print = N % 10
    while N > 0:
        if enable_print == 0 and N % 10 != 0:
            enable_print = 1
        elif enable_print !=0 or N % 10== 0:
            print(N % 10, end="")
            enable_print=1

        N = N // 10


debugVonage(100110)
