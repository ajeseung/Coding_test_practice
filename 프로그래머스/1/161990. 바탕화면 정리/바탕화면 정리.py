def solution(wallpaper):
    # 파일이 위치한 최소 및 최대 좌표를 찾기 위한 변수 설정
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = 0, 0

    # 파일 위치 찾기
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                min_x = min(min_x, i)
                min_y = min(min_y, j)
                max_x = max(max_x, i)
                max_y = max(max_y, j)
    
    # 드래그 끝점은 포함되지 않으므로 1을 더해줌
    return [min_x, min_y, max_x + 1, max_y + 1]