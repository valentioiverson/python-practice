import math
a, b = list(map(float, input().split(" ")))
boy_ratio = a/(a + b)
girl_ratio  = b/(a + b)
value = 0

for i in range(3,7):
    value += math.factorial(6)/(math.factorial(i)*math.factorial(6-i))*(boy_ratio ** i) * (girl_ratio ** (6 - i))

print(round(value,3))