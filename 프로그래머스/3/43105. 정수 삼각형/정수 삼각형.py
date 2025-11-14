def solution(triangle):
    # 아래에서 위로 올라가는 방식 (bottom-up)도 가능하지만,
    # 여기서는 위에서 아래로 내려가며 dp를 채움

    n = len(triangle)
    # dp 테이블을 triangle과 같은 모양으로 복사해도 되고,
    # triangle을 그대로 써도 됨 (in-place)
    dp = [[0] * len(row) for row in triangle]

    dp[0][0] = triangle[0][0]

    for i in range(1, n):          # 1행부터 마지막 행까지
        for j in range(i + 1):     # 각 행의 0 ~ i 열
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][i-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    return max(dp[-1])
