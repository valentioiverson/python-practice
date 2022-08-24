import math 

p = 0.12 
n = 10
value = 0
counter = 0
while counter <= 2:
    value += math.factorial(n)/(math.factorial(counter) * math.factorial(n - counter)) * (p ** counter) * ((1 - p) ** (n - counter))
    counter += 1
print(value)
# reset counter and value
counter = 0
value = 0
while counter <= 1:
    value += math.factorial(n)/(math.factorial(counter) * math.factorial(n - counter)) * (p ** counter) * ((1 - p) ** (n - counter))
    counter += 1
value = 1 - value
print(value)