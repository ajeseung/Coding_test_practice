def solution(strArr):
    n = len(strArr)
    arr = [0] * n
    
    for i in range(n):
        m = len(strArr[i])
        
        arr[m] += 1
        
    return max(arr)