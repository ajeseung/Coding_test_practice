def solution(A, B):
    n = len(A)
    cur = A
    for k in range(n):
        if cur == B:
            return k
        cur = cur[-1] + cur[:-1]  # 오른쪽으로 1칸 밀기
    return -1
