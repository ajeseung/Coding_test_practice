def solution(arr1, arr2):
    n, m, k = len(arr1), len(arr1[0]), len(arr2[0])
    result = [[0] * k for _ in range(n)]
    
    for i in range(n):
        for j in range(k):
            for t in range(m):
                result[i][j] += arr1[i][t] * arr2[t][j]
    return result
