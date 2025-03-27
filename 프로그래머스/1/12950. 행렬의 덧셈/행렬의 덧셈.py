def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):  # 각 행을 순회
        row = []
        for j in range(len(arr1[0])):  # 각 열을 순회
            row.append(arr1[i][j] + arr2[i][j])  # 같은 위치의 값 더하기
        result.append(row)  # 완성된 행을 결과에 추가
    return result
