def solution(maps):
    from collections import deque
    
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    results = []
    
    def bfs(r,c):
        queue = deque([(r,c)])
        visited[r][c] = True
        total_food = int(maps[r][c])
        
        while queue:
            x,y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    total_food += int(maps[nx][ny])
            
        return total_food
    
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] != 'X' and not visited[r][c]:
                results.append(bfs(r,c))
                
    if results:
        return sorted(results)
    else:
        return [-1]
