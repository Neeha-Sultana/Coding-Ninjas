from typing import *

def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    x=len(nums)-1
    arr1=[]
    while (x>=0):
        arr1.append(nums[x])
        x=x-1
    return arr1
