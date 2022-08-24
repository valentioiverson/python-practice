import numpy as np


firstarr = np.array([int(temp) for temp in input().split()])
secondarr = np.array([int(temp) for temp in input().split()])

print (np.inner(firstarr, secondarr))
print (np.outer(firstarr, secondarr))
