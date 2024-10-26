def solution(n, computers):
    def dfs(computer, visited, computers):
        # 현재 컴퓨터를 방문 처리
        visited[computer] = True
        # 현재 컴퓨터와 연결된 다른 컴퓨터를 재귀적으로 방문
        for connected_computer in range(n):
            if computers[computer][connected_computer] == 1 and not visited[connected_computer]:
                dfs(connected_computer, visited, computers)

    visited = [False] * n  # 방문 여부를 기록하는 배열
    network_count = 0  # 네트워크 개수를 기록하는 변수
    
    # 모든 컴퓨터를 탐색
    for computer in range(n):
        # 아직 방문하지 않은 컴퓨터라면 새 네트워크 발견
        if not visited[computer]:
            dfs(computer, visited, computers)
            network_count += 1  # 새로운 네트워크 발견 시 1 증가

    return network_count
