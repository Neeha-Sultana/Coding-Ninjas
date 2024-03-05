from typing import *
def factorialNumbers(n: int) -> List[int]:
    # Write your code here

    srr=[]

    s=1

    array_fact(s,n,srr)

    return srr

 

def array_fact(fact_num,original_num,arr):

    if return_fact(fact_num)>original_num:

        return arr

    arr.append(return_fact(fact_num))

    fact_num+=1

    array_fact(fact_num,original_num,arr)

 

def return_fact(n):

    if n==1:

        return 1

    return n * return_fact(n-1)
