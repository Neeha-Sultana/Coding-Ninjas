from math import *

def sumOfAllDivisors(n: int) -> int:
    summ = 0
    for i in range(1,n+1):
        
        for j in range(1,int(pow(i,0.5))+1):

            if i%j == 0:
                summ = summ + j

                if j != (i/j):
                    summ = summ + int(i/j)
    return summ
