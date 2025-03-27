def solution(n):
    n = str(n)
    m = sorted(n, reverse = True)
    
    print(m)
    
    return int(''.join(m))