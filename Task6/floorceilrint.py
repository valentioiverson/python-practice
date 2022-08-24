import numpy as np
np.set_printoptions(legacy='1.13')
templist = [float(temp) for temp in input().split()]
my_arr=np.array(templist)

print(np.floor(templist))
print(np.ceil(templist))
print(np.rint(templist))
