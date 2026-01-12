def solution(n):
    fact = 1
    i = 1

    while fact * i <= n:
        fact *= i
        i += 1

    return i - 1
