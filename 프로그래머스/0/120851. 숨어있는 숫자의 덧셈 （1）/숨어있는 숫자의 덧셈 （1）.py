def solution(my_string):
    n = len(my_string)
    answer = 0
    
    for i in range(n):
        if my_string[i].isdigit():
            my_int = int(my_string[i])
            answer += my_int
    return answer