def solution(myString, pat):
    cnt = 0
    
    p_len = len(pat)
    
    for i in range(len(myString) - p_len + 1):
        if myString[i:i+p_len] == pat:
            cnt += 1
            
    return cnt