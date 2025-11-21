def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    if n == 2:
        return max(sticker[0], sticker[1])
    
    # 경우 1: 0번 스티커를 사용한다 (n-1번은 못 씀)
    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])
    for i in range(2, n - 1):  # n-2까지
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    result1 = dp1[n-2]
    
    # 경우 2: 0번 스티커를 사용하지 않는다 (1 ~ n-1 사용 가능)
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    result2 = dp2[n-1]
    
    return max(result1, result2)
