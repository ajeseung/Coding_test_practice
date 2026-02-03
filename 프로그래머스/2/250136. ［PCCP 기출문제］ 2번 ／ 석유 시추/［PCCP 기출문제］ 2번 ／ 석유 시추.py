from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[False] * m for _ in range(n)]
    
    col_sum = [0] * m
    
    dr = (1, -1, 0, 0)
    dc = (0, 0, 1, -1)
    
    for r in range(n):
        for c in range(m):
            if land[r][c] == 1 and not visited[r][c]:
                q = deque([(r,c)])
                visited[r][c] = True
                
                cells = []
                touched_cols = set()
                
                while q:
                    x,y = q.popleft()
                    cells.append((x,y))
                    touched_cols.add(y)
                    
                    for k in range(4):
                        nx, ny = x + dr[k], y + dc[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if land[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                
                comp_size = len(cells)
                
                for col in touched_cols:
                    col_sum[col] += comp_size
                    
    return max(col_sum)