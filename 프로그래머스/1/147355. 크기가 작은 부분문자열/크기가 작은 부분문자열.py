def solution(t, p):
    k = len(p)
    target = int(p)
    
    count = 0
    
    for i in range(len(t) - k + 1):
        window = t[i:i+k]
        if int(window) <= target:
            count += 1
    return count