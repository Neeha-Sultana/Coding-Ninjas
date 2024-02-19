from typing import List

def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    for i in range(n-1, 0, -1):
        swapped = False
        for j in range(0, i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break        
    return arr 
    
