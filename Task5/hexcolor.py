import re

for _ in range(int(input())):
    check = re.findall( r'(?<=[ :])#[a-fA-F0-9]{3,6}', input())
    if check:
        print(*check, sep='\n')
