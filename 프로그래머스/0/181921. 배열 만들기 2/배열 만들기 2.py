def solution(l, r):
    answer = []
    for i in range(l, r+1):
        s = str(i)
        if all(ch in ('0', '5') for ch in s):
            answer.append(i)
            
    if not answer:
        return [-1]
    
    return answer
    