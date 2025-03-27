def solution(arr, divisor):
    m = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            m.append(arr[i])

    if len(m) == 0:
        return [-1]
    else:
        m.sort()
        return m