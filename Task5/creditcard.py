import re

for _ in range(int(input())):
    s = input()
    m = re.match(r'^([456]\d{3})-?(\d{4})-?(\d{4})-?(\d{4})$', s)
    m2 = re.search(r'([\d])\1{3}'
, s.replace("-", ""))
    print('Valid' if m and not m2 else 'Invalid')
