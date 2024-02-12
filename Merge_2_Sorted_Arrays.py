def sortedArray(a, b):
    i, j = 0, 0
    solution_list = []
    
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            solution_list.append(a[i])
            while i < len(a) - 1 and a[i] == a[i + 1]:
                i += 1
            while j < len(b) - 1 and b[j] == b[j + 1]:
                j += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            solution_list.append(a[i])
            while i < len(a) - 1 and a[i] == a[i + 1]:
                i += 1
            i += 1
        else:
            solution_list.append(b[j])
            while j < len(b) - 1 and b[j] == b[j + 1]:
                j += 1
            j += 1
    
    while i < len(a):
        solution_list.append(a[i])
        while i < len(a) - 1 and a[i] == a[i + 1]:
            i += 1
        i += 1
    
    while j < len(b):
        solution_list.append(b[j])
        while j < len(b) - 1 and b[j] == b[j + 1]:
            j += 1
        j += 1
    
    return solution_list
