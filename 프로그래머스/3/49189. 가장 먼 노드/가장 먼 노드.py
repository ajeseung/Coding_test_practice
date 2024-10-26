from collections import deque, defaultdict

def solution(n, vertex):
    # 그래프 인접 리스트 만들기
    graph = defaultdict(list)
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    # BFS를 위한 큐와 최단 거리 배열
    distance = [-1] * (n + 1)  # 각 노드까지의 최단 거리, -1로 초기화
    distance[1] = 0  # 1번 노드는 자기 자신이므로 거리 0
    queue = deque([1])  # BFS 시작점은 1번 노드

    # BFS 탐색
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if distance[neighbor] == -1:  # 아직 방문하지 않은 노드만 탐색
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    # 최댓값인 최단 거리를 찾고, 그 거리인 노드의 개수를 구함
    max_distance = max(distance)
    return distance.count(max_distance)
