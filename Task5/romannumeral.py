regex_pattern = r"^(?:(M){0,3})?(?:(D?(C){0,3})|(CM)|(CD))?(?:(L?(X){0,3})|(XC)|(XL))?(?:(V?(I){0,3})|(IX)|(IV))?$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))