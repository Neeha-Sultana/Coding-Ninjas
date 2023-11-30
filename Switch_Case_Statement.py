'''
from typing import *

def areaSwitchCase(ch: int, a: List[float]):
    # Write your code here
    if ch==1:
        r=a[0]
        dd=3.14*r*r
        return format(dd,'.5f')
    elif ch==2:
        de=a[0]*a[1]
        return format(de,'.5f')
        
    pass
'''

from typing import List

def areaSwitchCase(ch: int, a: List[float]) -> float:
    if ch == 1:
        r = a[0]
        return round(3.14159 * r * r, 5)
    elif ch == 2:
        return round(a[0] * a[1], 5)
