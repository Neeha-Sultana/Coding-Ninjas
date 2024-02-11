def rotateArray(arr: list, k: int) -> list:
    rev(arr,0,len(arr)-1)
    x=len(arr)-k
    rev(arr,0,x-1)
    rev(arr,x,len(arr)-1)
    return arr

def rev(arr,start,end):
    while(start<end):
        tempp=arr[start]
        arr[start]=arr[end]
        arr[end]=tempp
        start+=1
        end-=1
