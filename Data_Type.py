from typing import *
def dataTypes(type: str):
    if type=='Long':
        return 8
    elif type=='Integer':
        return 4
    elif type=='Float':
        return 4
    elif type=='Double':
        return 8
    elif type=='Character':
        return 1
    type=input()
    print(dataTypes(type))
