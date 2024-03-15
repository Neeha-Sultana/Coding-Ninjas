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
