def countDigits(n: int) -> int:
    x=n
    countt=0
    while(x>0):
        rem=x%10
        if rem!=0:
            if n%rem==0:
                countt+=1
        x=x//10
    return countt
