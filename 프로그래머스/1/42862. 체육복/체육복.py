def solution(n, lost, reserve):
    arr = [1] * n  
    for l in lost:
        arr[l - 1] -= 1 
    for r in reserve:
        arr[r - 1] += 1 

    for i in range(n):
        if arr[i] == 0:  
            if i > 0 and arr[i - 1] == 2:  
                arr[i] += 1
                arr[i - 1] -= 1
            elif i < n - 1 and arr[i + 1] == 2:  
                arr[i] += 1
                arr[i + 1] -= 1

    return sum(1 for x in arr if x > 0)
