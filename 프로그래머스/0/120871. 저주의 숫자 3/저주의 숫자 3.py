def solution(n):
    count = 0
    x = 0

    while count < n:
        x += 1

        # 3의 배수거나 숫자 3이 들어가면 스킵
        if x % 3 == 0 or '3' in str(x):
            continue

        count += 1

    return x
