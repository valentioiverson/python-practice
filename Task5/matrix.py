#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

temp = []
pattern = '((?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9]))'
for i in range(m):
    for j in matrix:
       temp.append(j[i])
res = ''.join(temp)
print(re.sub(pattern, ' ', res))
