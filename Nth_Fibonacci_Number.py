from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
a=1
b=1
i=1
n=int(input())
if n<=-1:
    print("False")
elif n==0:
    print(0)
elif n==1 or n==2:
    print(1)

else:
    while i<=n-2:
        c=a+b
        a=b
        b=c
        i=i+1
    print(c)
