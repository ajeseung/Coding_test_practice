N, M = map(int, input().split())

# 처음에는 바구니 번호와 같은 공이 들어있음
baskets = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    # swap
    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]

print(*baskets)
