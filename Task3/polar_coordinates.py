# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

number = complex(input())
phi = cmath.phase(number)
r = abs(number)

print(r)
print(phi)
