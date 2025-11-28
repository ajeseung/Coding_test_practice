def solution(intStrs, k, s, l):
    answer = []
    
    for x in intStrs:
        # s번 인덱스에서 시작하는 길이 l짜리 부분 문자열
        sub = x[s:s+l]
        num = int(sub)
        
        if num > k:
            answer.append(num)
    
    return answer
