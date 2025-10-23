from math import isqrt

def solution(n: int) -> int:
    # True/False 테이블 준비 (0과 1은 소수 아님)
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"

    # 에라토스테네스의 체
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            step = p
            # p의 배수들을 소수 아님으로 마킹
            sieve[start:n+1:step] = b"\x00" * (((n - start) // step) + 1)

    # True(=1) 개수가 곧 소수의 개수
    return sum(sieve)
