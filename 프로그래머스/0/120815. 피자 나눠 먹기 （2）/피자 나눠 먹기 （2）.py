def solution(n):
    r = 1
    while True:
        if (r*6) % n == 0:
            return r
        r += 1