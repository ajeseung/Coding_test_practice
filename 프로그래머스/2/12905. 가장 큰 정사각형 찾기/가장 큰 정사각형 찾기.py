def solution(board):
    n = len(board)
    m = len(board[0])

    # board를 그대로 dp로 써도 되지만, 원본을 안 건드리려면 따로 복사
    dp = [row[:] for row in board]

    max_side = 0

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                # 첫 행/첫 열은 그대로 0 또는 1
                max_side = max(max_side, dp[i][j])
            else:
                if board[i][j] == 1:
                    dp[i][j] = min(
                        dp[i-1][j],     # 위
                        dp[i][j-1],     # 왼쪽
                        dp[i-1][j-1]    # 좌상단 대각선
                    ) + 1
                    max_side = max(max_side, dp[i][j])
                # board[i][j]가 0이면 dp[i][j]는 이미 0이므로 그냥 둠

    return max_side *  max_side  # 넓이 = 변^2
