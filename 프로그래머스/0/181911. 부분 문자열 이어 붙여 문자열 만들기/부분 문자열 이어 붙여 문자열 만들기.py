def solution(my_strings, parts):
    result = []

    for s, (a, b) in zip(my_strings, parts):
        result.append(s[a:b+1])

    return ''.join(result)
