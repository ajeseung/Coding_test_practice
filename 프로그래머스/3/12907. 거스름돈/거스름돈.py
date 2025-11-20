def solution(n, money):
    MOD = 1_000_000_007
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for coin in money:
        for value in range(coin, n+1):
            dp[value] = (dp[value] + dp[value-coin]) % MOD
    
    return dp[n]