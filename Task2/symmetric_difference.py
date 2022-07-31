# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input())
firstset = set(list(map(int,input().split())))
N = int(input())
secondset = set(list(map(int,input().split())))
first_unique = list(firstset.difference(secondset))
second_unique = list(secondset.difference(firstset))
sym_dif = sorted(first_unique + second_unique)
for i in sym_dif:
    print(i)
