import numpy as np


N, M = map(int, input().split())
array = np.array([input().strip().split() for _ in range(N)], int)
print (array.transpose())
print (array.flatten())
