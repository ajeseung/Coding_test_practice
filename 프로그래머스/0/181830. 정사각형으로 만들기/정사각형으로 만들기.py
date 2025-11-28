def solution(arr):
    row = len(arr)
    col = len(arr[0])

    # 1. 열이 부족한 경우: 각 행에 0을 append
    if row > col:
        diff = row - col
        for r in arr:
            r.extend([0] * diff)

    # 2. 행이 부족한 경우: 새로운 행(길이 col)을 만들기
    elif row < col:
        diff = col - row
        for _ in range(diff):
            arr.append([0] * col)

    return arr
