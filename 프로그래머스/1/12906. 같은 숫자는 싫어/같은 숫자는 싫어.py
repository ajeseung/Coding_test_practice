def solution(arr):
    result = []
    
    # 첫 번째 값은 무조건 포함
    result.append(arr[0])
    
    # arr 배열을 순회하면서 연속된 숫자를 제거
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])
    
    return result
