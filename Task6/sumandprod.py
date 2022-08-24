import numpy as np

N, M = [int(temp) for temp in input().split()]
templist = []

for temp in range(N):
    templist.append([int(temp) for temp in input().split()])

myarr = np.array(templist)
print(np.prod(np.sum(myarr, axis = 0)))
