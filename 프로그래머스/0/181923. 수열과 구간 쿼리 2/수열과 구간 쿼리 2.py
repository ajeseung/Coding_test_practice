def solution(arr, queries):
    answer = []
    INF = 10**18
    
    for s,e,k in queries:
        best = INF
        for i in range(s,e+1):
            v = arr[i]
            if v > k and v < best:
                best = v
        
        answer.append(-1 if best == INF else best)
    return answer