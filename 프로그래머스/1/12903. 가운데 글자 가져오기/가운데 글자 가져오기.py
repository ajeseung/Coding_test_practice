def solution(s):
    l = len(s)
    
    m = l //2
    
    print(m)
    
    if l % 2 == 0:
        return s[m-1:m+1]
    else:
        return s[m]