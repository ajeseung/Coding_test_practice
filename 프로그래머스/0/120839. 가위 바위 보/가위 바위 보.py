def solution(rsp):
    answer = ''
    
    n = len(rsp)
    for i in range(n):
        if rsp[i] == '2':
            answer += '0'
        elif rsp[i] == '0':
            answer += '5'
        elif rsp[i] == '5':
            answer += '2'
    return answer