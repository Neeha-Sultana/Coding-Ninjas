def calcGDC(n:int, m: int) -> int:
    # Write your code here
    
   
    if n>=m:
        smal=m
    else:
        smal=n
    x=smal
    while(x>=1):
        if n%x==0 and m%x==0:
            return x
        x=x-1
        
