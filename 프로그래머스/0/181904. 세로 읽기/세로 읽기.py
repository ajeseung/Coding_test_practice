def solution(my_string, m, c):
    answer = ''
    n = len(my_string)
    
    for i in range(n):
        if i % m == c-1:
            answer += my_string[i]
    return answer