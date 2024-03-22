#Getting whole triangle
#Optimal 
from typing import *

def pascalTriangle(n : int) -> List[List[int]]:
    pas=[]
    for i in range(1,n+1):
        arr=[]
        for j in range(1,i+1):
            arr.append(ncr(i-1,j-1))
        pas.append(arr)
    return pas


def ncr(n,r):
    res=1
    for i in range(r):
        res=res*(n-i)
        res=res/(1+i)
    return int(res)
