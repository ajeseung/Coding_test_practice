from collections import defaultdict, deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    count = 1
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
                
    return count

def solution(n, wires):
    min_diff = float('inf')
    
    for i in range(len(wires)):
        # 그래프 초기화
        graph = defaultdict(list)
        
        # 현재 끊을 전선을 제외하고 그래프 구성
        for j in range(len(wires)):
            if i == j:
                continue
            v1, v2 = wires[j]
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        # BFS로 한쪽 네트워크의 송전탑 개수 계산
        visited = [False] * (n + 1)
        component_size = bfs(1, graph, visited)
        
        # 다른 네트워크의 송전탑 개수는 전체 n에서 component_size를 뺀 값
        other_component_size = n - component_size
        
        # 두 네트워크의 차이
        diff = abs(component_size - other_component_size)
        
        # 차이의 최솟값을 갱신
        min_diff = min(min_diff, diff)
    
    return min_diff
