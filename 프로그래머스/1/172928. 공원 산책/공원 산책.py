def solution(park, routes):
    H,W = len(park), len(park[0])
    
    direction = {"N": (-1,0), "S": (1,0), "E":(0,1), "W": (0,-1)}
    
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                x,y = i,j
                break
                
    for route in routes:
        dir, n = route.split()
        n = int(n)
        dx, dy = direction[dir]

        # 이동 가능 여부 체크
        nx, ny = x, y
        can_move = True
        for _ in range(n):
            nx += dx
            ny += dy
            if not (0 <= nx < H and 0 <= ny < W) or park[nx][ny] == 'X':
                can_move = False
                break

        # 이동 가능하면 위치 갱신
        if can_move:
            x, y = nx, ny

    return [x, y]
                