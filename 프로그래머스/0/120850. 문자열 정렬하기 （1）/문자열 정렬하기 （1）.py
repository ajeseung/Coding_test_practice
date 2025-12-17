def solution(my_string):
    numbers = []

    for ch in my_string:
        if ch.isdigit():
            numbers.append(int(ch))

    numbers.sort()
    return numbers