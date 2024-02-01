import numpy as np
import torch
import matplotlib.pyplot as plt

# 1D Tensor
inputList = [1, 2, 3, 4]
print(" =========== ")
print("Initiate Tensor")
print(" =========== ")
tensor1 = torch.Tensor(inputList)
print(tensor1)
print(tensor1.dtype)
print(tensor1.type())

print("  =========== ")
tensor1 = tensor1.type(torch.int32)
print("Tensor Changes to int")
print("  =========== ")
print(tensor1)
print(tensor1.dtype)
print(tensor1.type())

print("  =========== ")
print("Basic Function in Tensor")
print("  =========== ")
twoD_Tensor = tensor1.view(-1, 1)
print(twoD_Tensor)
print(twoD_Tensor[twoD_Tensor.size()[0] - 2].item())
tensorToList = tensor1.tolist()
print("Tensor to list" + str(tensorToList))

print("Change the Values of Tensor")
practice_tensor = torch.tensor([2, 7, 3, 4, 6, 2, 3, 1, 2])
print(practice_tensor)
selectedIndex = [3, 4, 7]
practice_tensor[selectedIndex] = 0
print(practice_tensor)

print("  =========== ")
print("Scientific Method Usage")
print("  =========== ")
pi = torch.linspace(start=1, end=np.pi, steps=4)
print(pi)
sinOfpi = torch.sin(pi)
print(sinOfpi)

u = torch.tensor([-1, 1])
v = torch.tensor([1, 1])
z = torch.dot(u, v)
print("Dot Function of u and v: " + str(z.item()))
