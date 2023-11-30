## Read input as specified in the question.
## Print output as specified in the question.
def alpi(x):
    if x>='A' and x<='Z':
        return 1
    elif x>='a' and x<='z':
        return 0
    else:
        return -1

x=input()
print(alpi(x))
