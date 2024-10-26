def solution(arrows):
    # 방향 벡터 설정
    directions = [ (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1) ]
    
    # 방문한 노드와 간선을 저장할 집합
    visited_nodes = set()
    visited_edges = set()
    
    # 초기 위치 (0, 0)에서 시작
    x, y = 0, 0
    visited_nodes.add((x, y))
    
    room_count = 0  # 방의 개수
    
    for arrow in arrows:
        # 방향에 따라 두번씩 이동하여 대각선 교차를 체크하기 위함
        for _ in range(2):
            dx, dy = directions[arrow]
            new_x, new_y = x + dx, y + dy
            
            # 간선 정보 생성
            current_edge = (x, y, new_x, new_y)
            reverse_edge = (new_x, new_y, x, y)
            
            if (new_x, new_y) in visited_nodes:
                # 노드를 방문한 적 있지만 간선을 방문한 적 없는 경우, 방이 생김
                if current_edge not in visited_edges and reverse_edge not in visited_edges:
                    room_count += 1
            else:
                # 새로운 노드 방문 처리
                visited_nodes.add((new_x, new_y))
            
            # 간선 방문 처리
            visited_edges.add(current_edge)
            visited_edges.add(reverse_edge)
            
            # 좌표 갱신
            x, y = new_x, new_y
    
    return room_count
