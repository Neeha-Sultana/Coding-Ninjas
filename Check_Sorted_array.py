def isSorted(n: int,  a: [int]) -> int:
    # Write youcode here.
    for i in range(1,len(a)):
        if a[i-1]>a[i]:
            x=False
            break
        x=True
    if x==True:
        return 1
    else:
        return 0



