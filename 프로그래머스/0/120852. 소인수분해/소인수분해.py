def solution(n):
    result = []
    
    i = 2
    while i <= n:
        if n % i == 0:
            result.append(i)
            n //= i
        else:
            i += 1
    
    return sorted(set(result))