import math 
from collections import *
from sys import *
from os import *

n = int(input())
counti = 0

# Loop until the square root of n
for i in range(2, int((n**0.5) + 1)):
    if n % i == 0:
        counti += 1
        break  # If a factor is found, no need to continue checking

if counti == 0 and n > 1:
    print("YES")  # Prime number has only 2 factors: 1 and itself
else:
    print("NO")

