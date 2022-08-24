import numpy as np
templist = [int(n) for n in input().split()]

arr1 = []
for temp in (range(templist[0])):
    arr1.append([int(temp) for temp in input().split()])

arr2 = []
for temp in (range(templist[0])):
    arr2.append([int(temp) for temp in input().split()])

a=np.array(arr1)   
b=np.array(arr2)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
