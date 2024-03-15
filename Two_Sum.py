"""
#Bruteforce
def read(n: int, book: [int], target: int) -> str:
    # Write your code here.
    for i in range(n):
        x=book[i]
        for j in range(n):
            if x+book[j]==target:
                return "YES"
    return "NO"
        
#Better
def read(n: int, book: [int], target: int) -> str:
    dict1={}
    for i in range(n):
        x=book[i]
        y=target-x
        if y in dict1:
            return "YES"
        else:
            dict1[x]=i
    return "NO"
"""
