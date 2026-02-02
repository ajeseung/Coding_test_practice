from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    grid = [list(row) for row in storage]
    EMPTY = '.'
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    def outside_empty_bfs():
        """바깥(경계)과 연결된 '빈 칸'을 BFS로 표시해서 visited 반환"""
        visited = [[False]*m for _ in range(n)]
        q = deque()

        # 경계의 빈 칸들에서 시작
        for i in range(n):
            for j in (0, m-1):
                if grid[i][j] == EMPTY and not visited[i][j]:
                    visited[i][j] = True
                    q.append((i, j))
        for j in range(m):
            for i in (0, n-1):
                if grid[i][j] == EMPTY and not visited[i][j]:
                    visited[i][j] = True
                    q.append((i, j))

        # 빈 칸끼리만 확장
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and grid[nx][ny] == EMPTY:
                        visited[nx][ny] = True
                        q.append((nx, ny))
        return visited

    for req in requests:
        ch = req[0]

        # 크레인: 해당 알파벳 전부 제거
        if len(req) == 2:
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == ch:
                        grid[i][j] = EMPTY
            continue

        # 지게차: "요청 시점" 접근 가능한 ch만 제거
        outside = outside_empty_bfs()
        to_remove = []

        for i in range(n):
            for j in range(m):
                if grid[i][j] != ch:
                    continue

                # 경계면은 무조건 접근 가능
                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    to_remove.append((i, j))
                    continue

                # 바깥과 연결된 빈 칸에 인접하면 접근 가능
                accessible = False
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if grid[ni][nj] == EMPTY and outside[ni][nj]:
                        accessible = True
                        break
                if accessible:
                    to_remove.append((i, j))

        # 동시 제거(연쇄 제거 방지)
        for i, j in to_remove:
            grid[i][j] = EMPTY

    # 남은 컨테이너 수
    return sum(1 for i in range(n) for j in range(m) if grid[i][j] != EMPTY)
