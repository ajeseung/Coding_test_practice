def solution(common):
    n = len(common)
    
    for i in range(n):
        if common[i+1] - common[i] == common[i+2] - common[i+1]:
            return common[n-1] + (common[i+1] - common[i])
        
        elif common[i+1] // common[i] == common[i+2] // common[i+1]:
            return common[n-1]*(common[i+1] // common[i])