def solution(my_string):
    answer = []
    n = len(my_string)

    for i in range(n):
        answer.append(my_string[i:])

    answer.sort()
    return answer
