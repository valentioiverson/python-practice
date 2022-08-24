import math

def cdf(mean, std, n):
    return  (1 + math.erf((n - mean) / (std * (2 ** 0.5)))) / 2


mean, std = list(map(float, input().split(' ')))
first = float(input().strip())
second = float(input().strip())
    
print(round((1-cdf(mean, std, first))*100, 2))
print(round((1-cdf(mean, std, second))*100, 2))
print(round(cdf(mean, std, second)*100, 2))