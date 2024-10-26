def solution(players, callings):
    # 선수의 이름을 키로 하고, 현재 순위를 값으로 저장하는 딕셔너리
    rank = {player: i for i, player in enumerate(players)}

    for call in callings:
        # 호출된 선수의 현재 순위를 가져옵니다.
        current_rank = rank[call]
        
        # 현재 순위에서 한 단계 위로 추월 (즉, 바로 앞 선수와 자리 교체)
        if current_rank > 0:  # 1등은 추월할 수 없으므로 체크
            # 추월할 선수의 이름을 가져옵니다.
            prev_player = players[current_rank - 1]
            
            # 선수들 순위 교환 (리스트와 딕셔너리 모두 업데이트)
            players[current_rank - 1], players[current_rank] = players[current_rank], players[current_rank - 1]
            rank[call] -= 1
            rank[prev_player] += 1

    return players
