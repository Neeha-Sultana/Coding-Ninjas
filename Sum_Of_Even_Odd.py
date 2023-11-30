## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
num=int(input())
x=num
sumeve=0
sumodd=0
while x>0:
    nn=x%10
    if nn%2==0:
        sumeve=sumeve+nn
    else:
        sumodd=sumodd+nn
    x=x//10
print(sumeve, sumodd, end='')
    


