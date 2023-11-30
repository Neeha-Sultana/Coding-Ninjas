'''
from typing import *

def compareIfElse(a: int, b: int):
    # Write your code here
    if a>b:
        return 'greater'
    elif a<b:
        return 'smaller'
    else:
        return"Equal"
    pass


a, b = map(int, input().split())
print(compareIfElse(a,b))
'''

from typing import *

def compareIfElse(a: int, b: int) -> str:
    if a > b:
        return 'greater'
    elif a < b:
        return 'smaller'
    else:
        return 'equal'

# Taking input from the user
