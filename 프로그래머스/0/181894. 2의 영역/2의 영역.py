def solution(arr):
    n = len(arr)
    first = -1
    last = -1

    # 첫 번째 2 찾기
    for i in range(n):
        if arr[i] == 2:
            first = i
            break

    # 2가 하나도 없는 경우
    if first == -1:
        return [-1]

    # 마지막 2 찾기
    for i in range(n - 1, -1, -1):
        if arr[i] == 2:
            last = i
            break

    # first ~ last까지 잘라서 리턴
    return arr[first:last + 1]
