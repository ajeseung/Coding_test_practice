from itertools import combinations

def solution(nums):
    # 1) 합의 최댓값 계산 (여유 있게 3000으로 잡아도 됨)
    max_sum = 3000

    # 2) 에라토스테네스의 체로 소수 테이블 생성
    is_prime = [False, False] + [True] * (max_sum - 1)  # 0,1은 소수 아님
    for p in range(2, int(max_sum ** 0.5) + 1):
        if is_prime[p]:
            for q in range(p*p, max_sum + 1, p):
                is_prime[q] = False

    # 3) 서로 다른 3개 조합의 합이 소수인지 카운트
    count = 0
    for a, b, c in combinations(nums, 3):
        s = a + b + c
        if is_prime[s]:
            count += 1
    return count
