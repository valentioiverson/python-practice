import numpy as np 
N = int(input())
newarr = np.array([list(map(float,input().split()))for i in range(N)])
print(round(np.linalg.det(newarr),2))
