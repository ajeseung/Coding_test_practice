def solution(my_string, is_prefix):
    n = len(is_prefix)
    m = len(my_string)
    
    if m < n:
        return 0
    
    
    for i in range(n):
        if my_string[i] != is_prefix[i]:
            return 0
    
    return 1