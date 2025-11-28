def solution(q, r, code):
    answer = ''
    n = len(code)
    
    for i in range(n):
        if i % q == r:
            answer += code[i]
            
    return answer