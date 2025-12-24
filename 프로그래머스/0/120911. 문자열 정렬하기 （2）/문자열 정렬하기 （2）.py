def solution(my_string):
    lower = my_string.lower()
    sorted_chars = sorted(lower)
    answer = ''.join(sorted_chars)
    return answer
