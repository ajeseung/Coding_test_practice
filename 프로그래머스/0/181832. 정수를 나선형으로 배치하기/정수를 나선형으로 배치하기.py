def solution(n):
    board = [[0] * n for _ in range(n)]

    # 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r, c, d = 0, 0, 0  # 시작 위치, 시작 방향(오른쪽)

    for val in range(1, n * n + 1):
        board[r][c] = val

        nr = r + dr[d]
        nc = c + dc[d]

        # 다음 칸이 범위 밖이거나 이미 채워졌으면 방향 전환
        if not (0 <= nr < n and 0 <= nc < n) or board[nr][nc] != 0:
            d = (d + 1) % 4
            nr = r + dr[d]
            nc = c + dc[d]

        r, c = nr, nc

    return board
