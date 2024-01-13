from typing import *

def countFrequency(n: int, m: int, edges: List[List[int]]):
    countt=0
    arr=[]
    for i in range(1,len(edges)+1):
        countt=0
        for j in range(len(edges)):
            if edges[j]==i:
                countt+=1
        arr.append(countt)
    return arr
