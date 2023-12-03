from os import *
from sys import *
from collections import *
from math import *

n=input()
numb=int(n)
x=len(n)
summ=0
while numb>0:
    dig=numb%10
    summ=summ+dig**x
    numb=numb//10

if summ==int(n):
    print('true')
else:
    print("false")
