from collections import deque

def solution(board):
    # 보드 크기
    H, W = len(board), len(board[0])
    
    # 이동 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 로봇(R)과 목표(G) 위치 찾기
    start, goal = None, None
    for i in range(H):
        for j in range(W):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)
    
    # BFS 초기화
    queue = deque([(start[0], start[1], 0)])  # (현재 행, 현재 열, 이동 횟수)
    visited = set([start])

    # BFS 탐색 시작
    while queue:
        x, y, moves = queue.popleft()
        
        # 목표 위치 도달 시 최소 이동 횟수 반환
        if (x, y) == goal:
            return moves
        
        # 4방향 이동
        for dx, dy in directions:
            nx, ny = x, y

            # 장애물이나 벽을 만나기 전까지 미끄러짐
            while 0 <= nx + dx < H and 0 <= ny + dy < W and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy
            
            # 방문하지 않은 위치라면 큐에 추가
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1))

    # 목표 지점에 도달할 수 없는 경우
    return -1