def solution(array, n):
    arr = []
    
    for num in array:
        arr.append(abs(n - num))
    
    min_val = min(arr)
    
    candidates = []
    
    for i in range(len(arr)):
        if arr[i] == min_val:
            candidates.append(array[i])
    
    return min(candidates)
