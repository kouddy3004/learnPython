x=int(input("Enter "))
prime= True
for i in range(2,x):
    if(x%i==0 and i!=x):
        prime=False
        break

if(prime==True):
    print(str(x)+" is prime")
else:
    print(str(x)+" is not prime")

    
