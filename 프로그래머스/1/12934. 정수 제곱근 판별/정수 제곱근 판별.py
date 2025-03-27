def solution(n):
    x = n ** 0.5
    
    if x % 1 == 0:
        return (x+1) * (x+1)
    else:
        return -1