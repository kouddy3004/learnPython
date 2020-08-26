list = [1,2,3,2,1]
for i in range(len(list)):
    for j in range(i):
        if(list[i]==list[j]):
            print(str(list[i])+" is duplicate")

