def solution(n, times):
    low = 1
    high = max(times) * n
    
    answer = high
    
    while low <= high:
        mid = (low + high) // 2
        
        people = 0
        for t in times:
            people += mid // t
            
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return answer