def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    
    result = 0
    
    for a, b in zip(A,B):
        result += a* b
        
    return result