import numpy as np


N, M = [int(temp) for temp in input().split()]

templist = []
for temp in range(N):
    templist.append([int(temp) for temp in input().split()])
myarr = np.array(templist)

myarr_mean = np.mean(myarr, axis = 1)
myarr_var = np.var(myarr, axis = 0)
myarr_std = np.std(myarr)
print(myarr_mean, myarr_var, round(myarr_std, 11), sep = "\n")

