# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
AB = float(input())
BC = float(input())
print(str(int(round(math.degrees(math.atan(AB/BC)),0)))+'\u00B0')
