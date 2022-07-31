# Enter your code here. Read input from STDIN. Print output to STDOUT

set_A = set(map(int, input().split()))
result = "True"; 
for i in range(int(input())):
    set_B = set(map(int,input().split()))
    if len(set_B.intersection(set_A)) < len(set_B):
        result = "False"; 
print(result)
