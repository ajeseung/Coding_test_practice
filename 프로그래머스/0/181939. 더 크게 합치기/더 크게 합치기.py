

def solution(a, b):
    a1 = str(a)
    b1 = str(b)
    
    i = int(a1+b1)
    j = int(b1+a1)
    
    if i >= j:
        return i
    else:
        return j