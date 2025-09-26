def solution(a, d, included):
    total = 0
    
    for i, bl in enumerate(included):
        if bl:
            total += a + i*d
    return total