from typing import List
l=list()
def printNos(x: int) -> List[int]: 
    # Write your code here
    if x<1:
        return
    else:

        
        #l.append(x)
        printNos(x-1)
        l.append(x)
    return l




