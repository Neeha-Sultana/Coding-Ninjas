n=int(input())  
# taking n as a input 
## write your code !!
x=n
pal=0
while(x>0):
    dig=x%10
    pal=pal*10+dig
    x=x//10

if n==pal:
    print('true')
else:
    print('false')
