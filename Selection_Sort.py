from typing import List

def selectionSort(arr: List[int]) -> None: 
    for i in range(len(arr)):
        sm = arr[i]
        x = i

        for j in range(i+1, len(arr)):
            if sm > arr[j]:
                sm = arr[j]
                x = j

        # Move the following two lines outside the inner loop
        arr[x] = arr[i]
        arr[i] = sm
    return arr
