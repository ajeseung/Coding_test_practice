N, M = map(int, input().split())

baskets = [0] * N  # 1번 ~ N번 바구니, 처음엔 전부 0

for _ in range(M):
    i, j, k = map(int, input().split())
    # i, j는 1부터 시작하니까 인덱스로 쓸 때는 -1 해줌
    for idx in range(i - 1, j):
        baskets[idx] = k

print(*baskets)
