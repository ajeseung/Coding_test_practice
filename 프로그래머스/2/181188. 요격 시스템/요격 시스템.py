def solution(targets):
    # 폭격 미사일을 종료 지점(e) 기준으로 정렬
    targets.sort(key=lambda x: x[1])
    
    count = 0  # 요격 미사일 개수
    last_shot = -1  # 마지막 요격 지점 (초기값: 요격되지 않은 상태)
    
    for s, e in targets:
        # 현재 요격 지점이 이 미사일의 범위에 포함되지 않으면 새로운 미사일 발사
        if last_shot < s:
            count += 1  # 새로운 요격 미사일 추가
            last_shot = e - 0.5  # 종료 지점 직전에서 요격 (개구간이므로 e는 포함되지 않음)
    
    return count
