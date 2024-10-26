from collections import deque

def solution(maps):
    # 네 가지 이동 방향: 동, 서, 남, 북
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # 맵의 크기
    n = len(maps)    # 세로 길이
    m = len(maps[0]) # 가로 길이
    
    # BFS를 위한 큐 초기화: (현재 위치 x, y, 현재까지의 이동 칸 수)
    queue = deque([(0, 0, 1)])  # 시작 지점 (0, 0)에서 출발하며, 첫 번째 칸은 1칸 이동
    
    # 방문 처리 배열
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True  # 시작점 방문 처리
    
    while queue:
        x, y, distance = queue.popleft()
        
        # 목표 위치에 도달했을 때 최단 거리 반환
        if x == n - 1 and y == m - 1:
            return distance
        
        # 네 가지 방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 이동할 위치가 맵의 범위 내에 있고, 벽이 아니며, 아직 방문하지 않았다면
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문 처리
                queue.append((nx, ny, distance + 1))  # 큐에 다음 경로 추가
    
    # 도착점에 도달할 수 없는 경우
    return -1
