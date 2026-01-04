def solution(arr, intervals):
    result = []
    
    arr1 = intervals[0]
    arr2 = intervals[1]
    
    a = arr1[0]
    b = arr1[1]
    c = arr2[0]
    d = arr2[1]
    
    for i in range(a,b+1):
        result.append(arr[i])
    for j in range(c,d+1):
        result.append(arr[j])
        
    return result