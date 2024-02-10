"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""
from typing import List

def quickSort(arr: List[int], startIndex: int, endIndex: int):
    if startIndex<endIndex:
        piv=partition(arr,startIndex,endIndex)
        quickSort(arr,startIndex,piv-1)
        quickSort(arr,piv+1,endIndex)
    


def partition(arr,startIndex,endIndex):
    i=startIndex
    j=endIndex
    pi=arr[startIndex]
    while i<j:
        while(arr[i]<=pi and i<=endIndex-1):
            i+=1
        while(arr[j]>pi and j>=startIndex+1):
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[startIndex],arr[j]=arr[j],arr[startIndex]

    return j
