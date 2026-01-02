def solution(arr, n):
    result = []
    if len(arr) % 2 == 1:
        for i in range(len(arr)):
            result.append(arr[i] + n if i % 2 == 0 else arr[i])
    else:
        for i in range(len(arr)):
            result.append(arr[i] + n if i % 2 == 1 else arr[i])
    return result