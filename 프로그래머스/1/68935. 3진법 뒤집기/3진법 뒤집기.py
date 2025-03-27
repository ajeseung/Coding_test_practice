def solution(n):
    # 1. 10진수 → 3진수
    t = ''
    while n > 0:
        n, r = divmod(n, 3)
        t += str(r)  # 뒤집힌 상태로 누적

    # 2. 이미 뒤집힌 상태로 만들어졌으므로 바로 10진수 변환
    return int(t, 3)