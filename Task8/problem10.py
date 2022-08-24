import numpy as np

m, n = map(int, input().split())
temp = [list(map(float, input().split())) for _ in range(n)]
y = np.array([x.pop() for x in temp])
X = np.array(temp)
b = np.ones(n)
X = np.c_[b, X]


var = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
counter = int(input())
for _ in range(counter):
    k = np.array(input().split(), float)
    print(round(var.dot(np.insert(k, 0, 1)),2))