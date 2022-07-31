# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):
    size_A = int(input())
    set_A = set(input().split())
    size_B = int(input())
    set_B = set(input().split())
    print(set_B.intersection(set_A) == set_A)
