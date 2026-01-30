def solution(my_string):
    result = []
    for ch in my_string:
        if ch.islower():
            result.append(ch.upper())
        else:  # 대문자
            result.append(ch.lower())
    return ''.join(result)
