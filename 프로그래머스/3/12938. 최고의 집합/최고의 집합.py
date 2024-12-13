def solution(n, s):
    if s < n:
        return [-1]
    
    answer = [s//n]*n
    remain = s%n
    
    for i in range(remain):
        answer[-1-i] +=1
    
    return answer