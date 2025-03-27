def solution(x):
    a= str(x)
    
    m = sum(int(d) for d in a)
    
    print(m)
    
    if x % m == 0:
        return True
    else:
        return False