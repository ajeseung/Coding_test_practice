def solution(num_list):
    answer = []
    odds = 0
    even = 0
    
    for num in num_list:
        if num % 2 == 1:
            odds += 1
        else:
            even += 1
    answer.append(even)
    answer.append(odds)
    
    return answer