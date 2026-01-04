def solution(numbers, n):
    answer = 0
    m = len(numbers)
    
    for i in range(m):
        answer += numbers[i]
        if answer > n:
            break
    return answer