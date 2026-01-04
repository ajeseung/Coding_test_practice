def solution(arr):
    result = []
    n = len(arr)
    
    for i in range(n):
        k = arr[i]
        for j in range(k):
            result.append(k)
    
    return result