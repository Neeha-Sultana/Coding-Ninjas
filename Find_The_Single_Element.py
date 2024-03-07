from typing import *
def getSingleElement(arr : List[int]) -> int:
    dict1={}
    for i in range(len(arr)):
        if arr[i] not in dict1:
            dict1[arr[i]]=1
        else:
            dict1[arr[i]]+=1
    
    for key,values in dict1.items():
        if values==1:
            return key
