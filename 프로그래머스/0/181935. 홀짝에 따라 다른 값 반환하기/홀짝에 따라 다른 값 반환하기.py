def solution(n):
    answer = 0
    if n % 2 ==1:
        for j in range (n+1):
            if j % 2 == 1:
                answer += j
            else:
                answer += 0
    
    else:
        for i in range (n+1):
            if i % 2 == 1:
                answer += 0
            else:
                answer += i*i
                
    return answer