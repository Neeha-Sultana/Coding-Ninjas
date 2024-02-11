from sys import *
from collections import *
from math import *

def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    a=[]
    for i in range(n):
        a.append(arr[i])
    
    for i in range(0,n):
        a[(i-1)%n]=arr[i]
    return a

