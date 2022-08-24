import math

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

def findmean(templist, size): 
    temp = sum(templist)/size
    return temp

def findstd(templist, size):
    mean = findmean(templist, size)
    count = 0
    for temp in templist: 
        count += (temp - mean) ** 2
    std = (count/n) ** 0.5
    return std


def findcov(X, Y, n): 
    X_mean = findmean(X, n)
    Y_mean = findmean(Y, n)
    count = 0
    for x, y in zip(X,Y):
        count += (x - X_mean)*(y - Y_mean)
    temp = count / n
    return temp


cov = findcov(X, Y, n)
std_x = findstd(X,n)
std_y = findstd(Y, n)
print(round( cov / (std_x * std_y), 3))