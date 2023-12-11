from  typing import *

def printNtimes(n: int) -> None:
    if n<=0:
        return
    printNtimes(n-1)
    print("Coding Ninjas ",end=' ')
