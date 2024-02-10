def getSecondOrderElements(n: int, a: [int]) -> [int]:
    # Write your code here.
    
    lar = a[0]
    smal = a[0]
    secondlar = float('-inf')  # Initialize to negative infinity
    secsmal = float('inf')     # Initialize to positive infinity
    
    for i in range(len(a)):
        if a[i] > lar:
            secondlar = lar
            lar = a[i]
        elif a[i] < lar and a[i] > secondlar:
            secondlar = a[i]

    for i in range(len(a)):
        if a[i] < smal:
            secsmal = smal
            smal = a[i]
        elif a[i] > smal and a[i] < secsmal:
            secsmal = a[i]
    
    return secondlar, secsmal

