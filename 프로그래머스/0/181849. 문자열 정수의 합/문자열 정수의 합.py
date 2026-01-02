def solution(num_str):
    answer = 0
    n = len(num_str)
    for i in range(n):
        answer += int(num_str[i])
    return answer