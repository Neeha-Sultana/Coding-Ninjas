from sys import *
from collections import *
from math import *
def largestElement(arr: [], n: int) -> int:
    lar=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>lar:
            lar=arr[i]

    return lar
