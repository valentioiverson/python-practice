import numpy as np


N = int(input())

templist = []
for temp in range(N):
    templist.append([int(temp) for temp in input().split()])
firstarr = np.array(templist)

templist = []
for temp in range(N):
    templist.append([int(temp) for temp in input().split()])
secondarr = np.array(templist)


print(np.dot(firstarr, secondarr))
