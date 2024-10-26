from collections import deque

# 좌표 2배 확장 및 BFS 탐색을 위한 함수 정의
def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표 확장 및 맵 크기 설정
    board = [[-1] * 102 for _ in range(102)]  # 50 x 50을 2배 확장하여 100 x 100 맵

    # 좌표 확장
    for x1, y1, x2, y2 in rectangle:
        for i in range(2 * x1, 2 * x2 + 1):
            for j in range(2 * y1, 2 * y2 + 1):
                if x1 * 2 < i < x2 * 2 and y1 * 2 < j < y2 * 2:  # 내부는 0으로 표시
                    board[i][j] = 0
                elif board[i][j] != 0:  # 테두리는 1로 표시
                    board[i][j] = 1

    # BFS 탐색
    def bfs():
        q = deque([(characterX * 2, characterY * 2, 0)])  # 시작 위치 (확장 후 좌표) 및 이동 거리
        visited = [[False] * 102 for _ in range(102)]
        visited[characterX * 2][characterY * 2] = True

        # 상하좌우 방향
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            x, y, dist = q.popleft()

            # 아이템을 찾으면 거리 반환
            if x == itemX * 2 and y == itemY * 2:
                return dist // 2  # 좌표를 2배 확장했으므로 실제 거리는 절반

            # 상하좌우로 이동
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 102 and 0 <= ny < 102 and not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))

    # BFS를 통해 최소 이동 거리 계산
    return bfs()
