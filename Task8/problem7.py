n = int(input())
mu = int(input())
sigma = int(input())
prob = float(input())
z = float(input())
    
temp = sigma / (n**(1 - prob))
    
print(mu-(z*temp))
print(mu+(z*temp))