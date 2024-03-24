'''
#bruteforce
from typing import *
def subarrayWithMaxProduct(arr : List[int]) -> int:
    # Write your code here.
    lar=float('-inf')
    if len(arr)==0:
        return 0
    elif len(arr)==1:
        return arr[0]
    else:
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                prod=1
                for k in range(i,j+1):
                    prod=prod*(arr[k])
                    if prod>lar:
                        lar=prod
        return lar

#better
from typing import *
def subarrayWithMaxProduct(arr : List[int]) -> int:
    res=arr[0]
    for i in range(len(arr)-1):
        prod=arr[i]
        for j in range(i+1,len(arr)):
            res = max(res, prod)
            prod *= arr[j]
        res = max(res, prod)

    return res
'''

#optimal
from typing import *
def subarrayWithMaxProduct(arr : List[int]) -> int:
    pre=1
    suf=1
    ans=-float("inf")
    for i in range(len(arr)):
        if pre==0 :
            pre=1
        elif suf==0:
            suf=1
        pre=pre*arr[i]
        suf=suf*arr[len(arr)-i-1]

        ans=max(ans,max(suf,pre))
    return ans
