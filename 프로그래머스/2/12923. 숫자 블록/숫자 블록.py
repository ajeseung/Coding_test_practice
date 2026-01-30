from math import isqrt

def solution(begin, end):
    MAX_N = 10_000_000
    result = []

    for x in range(begin, end + 1):
        if x == 1:
            result.append(0)
            continue

        best = 1  # 최소 약수 1은 항상 후보

        limit = isqrt(x)
        for d in range(2, limit + 1):
            if x % d == 0:
                q = x // d

                # 10,000,000 이하인 가장 큰 약수를 찾고 싶으므로
                # q부터 체크한다.
                if q <= MAX_N:
                    best = q
                    break

                # q가 너무 크면, d 쪽도 후보가 될 수 있음
                if d <= MAX_N:
                    best = d

        result.append(best)

    return result
