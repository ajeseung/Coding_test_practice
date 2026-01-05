# def solution(n):
#     count = 0
#     k = 1
#     while k * (k - 1) // 2 < n:
#         if (n - (k * (k - 1) // 2)) % k == 0:
#             count += 1
#         k += 1
#     return count

def solution(n):
    count = 0
    for i in range(1, n + 1, 2):  # 홀수만 확인
        if n % i == 0:
            count += 1
    return count

