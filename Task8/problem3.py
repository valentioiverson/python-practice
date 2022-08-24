import math

def cdf(mean, std, n):
    return  (1 + math.erf((n - mean) / (std * (2 ** 0.5)))) / 2

mean, std = list(map(float, input().split(' ')))
first = float(input().strip())
second, third = list(map(float, input().split(' ')))
    
print(round(cdf(mean, std, first), 3))
print(round(cdf(mean, std, third) - cdf(mean, std, second), 3))