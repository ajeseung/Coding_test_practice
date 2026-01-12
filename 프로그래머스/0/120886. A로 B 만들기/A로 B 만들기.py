def solution(before, after):
    b = sorted(before)
    a = sorted(after)
    
    if b == a:
        return 1
    else:
        return 0