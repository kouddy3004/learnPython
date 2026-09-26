x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original Value :" + str(x))
# list Flattten
y = [j for i in x for j in i]
print("List Flatten")
print(y)

x = [11, 6, 1, 10, 4, 8, 3, 9]
print("\nOriginal Value : " + str(x))
size = len(x)
for i in range(size):
    for j in range(size - i - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]
print("Sorted Value :" + str(x))


def square(**kwargs):
    a = []
    for val in kwargs.values():
        a.append((val * val))
    return a


a = square(a=1, b=4)
print("\nUsed **kwargs to get Squares of two argument(a=1, b=4) : " + str(a))

# Square using lambda
squareLambda = list(map(lambda i: i * i if i % 2 == 0 else i, x))
print("Squaring the lists if it's even using lambda : " + str(squareLambda))

# Check filter in lambda

# Reduce
from functools import reduce

print("Adding all the values in a list : " + str(reduce(lambda x, y: x + y, x)))

# Decorator

# Generator
