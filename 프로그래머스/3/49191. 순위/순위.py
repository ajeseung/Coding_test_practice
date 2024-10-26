def solution(n, results):
    # 승패 정보를 기록할 2차원 배열 생성 (플로이드-워셜을 적용할 그래프)
    # -1은 초기값(모름), 1은 승리, 0은 패배
    dist = [[0] * (n + 1) for _ in range(n + 1)]
    
    # 주어진 경기 결과로 승패 관계를 기록
    for win, lose in results:
        dist[win][lose] = 1  # win 선수가 lose 선수를 이겼다.
        dist[lose][win] = -1 # lose 선수가 win 선수에게 졌다.
    
    # 플로이드-워셜 알고리즘 적용
    for k in range(1, n + 1):  # 중간 선수 k
        for i in range(1, n + 1):  # 시작 선수 i
            for j in range(1, n + 1):  # 끝 선수 j
                if dist[i][k] == 1 and dist[k][j] == 1:
                    dist[i][j] = 1  # i 선수가 k 선수를 이기고, k 선수가 j 선수를 이겼다면 i는 j도 이긴다
                    dist[j][i] = -1 # j 선수는 i 선수에게 진다
    
    # 순위를 확정할 수 있는 선수 세기
    answer = 0
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if dist[i][j] != 0:  # 승패가 결정된 경우 카운트
                count += 1
        if count == n - 1:  # 나를 제외한 모든 선수와의 승패가 결정된 경우
            answer += 1
    
    return answer
