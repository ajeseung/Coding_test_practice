def solution(players, m, k):
    n = len(players)  # 24시간 기준
    running_servers = [0] * n  # 각 시간대에 새롭게 추가된 서버 수
    total_additions = 0  # 총 서버 증설 횟수
    
    active_servers = 0  # 현재 운영 중인 서버 수
    
    for hour in range(n):
        # k시간 전에 추가된 서버가 만료되면 제거
        if hour >= k:
            active_servers -= running_servers[hour - k]
        
        # 현재 필요한 서버 수 계산
        required_servers = players[hour] // m
        
        # 부족한 서버 수 계산
        if required_servers > active_servers:
            new_servers = required_servers - active_servers
            total_additions += new_servers
            running_servers[hour] = new_servers  # 현재 시간에 추가된 서버 기록
            active_servers += new_servers  # 운영 중인 서버 수 업데이트
    
    return total_additions