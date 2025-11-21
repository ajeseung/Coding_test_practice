import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    
    # 그래프 구성
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    INF = float('inf')
    dist = [INF] * (N+1)
    dist[1] = 0
    
    pq = [(0, 1)]  # (시간, 노드)
    
    # 다익스트라
    while pq:
        time, node = heapq.heappop(pq)
        if dist[node] < time:
            continue
        
        for nxt, cost in graph[node]:
            new_time = time + cost
            if new_time < dist[nxt]:
                dist[nxt] = new_time
                heapq.heappush(pq, (new_time, nxt))
    
    # K 이하인 마을 개수 반환
    return sum(1 for d in dist if d <= K)
