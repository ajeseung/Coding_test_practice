def solution(n, stations, w):
    answer = 0
    cover = 2*w + 1
    pos = 1
    idx = 0
    
    while pos <= n:
        if idx < len(stations) and stations[idx] - w <= pos <= stations[idx] + w:
            # 이 기지국이 덮을 수 있는 끝 다음으로 점프
            pos = stations[idx] + w + 1
            idx += 1
        # 2) 아직 안 나온 다음 기지국이 있고, 그 기지국의 커버 시작이 pos보다 뒤에 있는 경우
        elif idx < len(stations) and pos < stations[idx] - w:
            # pos ~ (stations[idx] - w - 1) 까지가 빈 구간
            gap_len = (stations[idx] - w) - pos
            # gap_len 을 cover 로 나누어서 필요한 개수 계산
            need = (gap_len + cover - 1) // cover
            answer += need
            pos += need * cover
        # 3) 더 이상 기지국이 없는 경우 → 끝까지 빈 구간
        else:
            gap_len = n - pos + 1
            need = (gap_len + cover - 1) // cover
            answer += need
            break

    return answer
