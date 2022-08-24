import math 

def cdf(mean, std, n):
    return  (1 + math.erf((n - mean) / (std * (2 ** 0.5)))) / 2

max_weight = float(input())
n = int(input())
mu = float(input())
std = float(input())
new_mean = n * mu
new_std = std * ( n ** 0.5)
value = round(cdf(new_mean, new_std, max_weight), 4)
print(value)