import re
for _ in range(int(input())):
    temp = input()
    print("Valid" if len(re.findall(r"[A-Z]",temp))>=2 and len(re.findall(r"[0-9]",temp))>=3 and len(re.findall(r"[\w]",temp))==len(temp) and len(re.findall(r"(\w)\1","".join(sorted(temp))))==0 and len(temp)==10 else "Invalid") 
