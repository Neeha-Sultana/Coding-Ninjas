def removeDuplicates(arr,n):
    ct=0
    for i in range(n-1):
        if arr[i]!=arr[i+1]:
            ct+=1
        else:
            continue

    return ct+1
arr=[1,2,2,2,4,5,6,6,11,11,12,23]
print(removeDuplicates(arr,len(arr)))
