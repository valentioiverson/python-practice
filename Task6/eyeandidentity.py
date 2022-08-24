import numpy as np
np.set_printoptions(legacy='1.13')

N, M = map(int, input().strip().split())
print(np.eye(N,M))

