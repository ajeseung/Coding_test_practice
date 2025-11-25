N = int(input())

# 위쪽 (1 ~ N)
for i in range(1, N + 1):
    print(" " * (N - i) + "*" * (2 * i - 1))

# 아래쪽 (N-1 ~ 1)
for i in range(N - 1, 0, -1):
    print(" " * (N - i) + "*" * (2 * i - 1))
