import re
vowel = "aeiou"
cons = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (cons, vowel, cons), input(), flags = re.I)
print('\n'.join(m or ['-1']))
