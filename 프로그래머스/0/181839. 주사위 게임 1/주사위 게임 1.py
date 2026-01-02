def solution(a, b):
    m = (a%2) + (b%2)
    
    if m == 2:
        return a*a + b*b
    elif m == 1:
        return 2*(a+b)
    else:
        return abs(a-b)