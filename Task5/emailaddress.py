import re

n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    check = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if check:
        print(x,y)
