def solution(names):
    n = len(names)
    result = []
    
    for i in range(n):
        if i % 5 == 0:
            result.append(names[i])
            
    return result