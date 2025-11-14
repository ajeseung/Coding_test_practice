def solution(m, n, puddles):
    MOD = 1000000007
    
    # dp[y][x] : (x, y)까지 오는 경우의 수
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 웅덩이 표시
    puddle_set = set((x, y) for x, y in puddles)
    
    dp[1][1] = 1  # 시작점
    
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if (x, y) in puddle_set:
                dp[y][x] = 0  # 웅덩이는 경로 불가
                continue
            if x == 1 and y == 1:
                continue  # 시작점은 이미 1로 설정됨
            
            dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % MOD
    
    return dp[n][m]
