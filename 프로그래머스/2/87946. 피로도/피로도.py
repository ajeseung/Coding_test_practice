from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    
    # 모든 던전 탐험 순서에 대해 순열을 생성
    for perm in permutations(dungeons):
        current_k = k  # 현재 피로도
        count = 0  # 탐험한 던전 수
        
        # 탐험 가능한지 순서대로 확인
        for dungeon in perm:
            min_fatigue, consume_fatigue = dungeon
            if current_k >= min_fatigue:
                current_k -= consume_fatigue
                count += 1
            else:
                break  # 피로도가 부족하면 더 이상 탐험할 수 없음
        
        # 최대 탐험 가능한 던전 수 갱신
        max_dungeons = max(max_dungeons, count)
    
    return max_dungeons
