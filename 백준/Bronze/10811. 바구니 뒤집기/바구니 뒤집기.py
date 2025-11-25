N, M = map(int, input().split())

# 1번 바구니부터 N번 바구니까지 번호 그대로 들어있는 상태
baskets = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    # i, j는 1부터 시작하니까 인덱스는 i-1, j-1
    # i-1 ~ j-1 구간을 역순으로 교체
    baskets[i-1:j] = reversed(baskets[i-1:j])

print(*baskets)
