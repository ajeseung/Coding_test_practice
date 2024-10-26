import heapq

def solution(scoville, K):
    # 최소 힙으로 변환
    heapq.heapify(scoville)
    
    mix_count = 0
    
    # 가장 작은 스코빌 지수가 K 이상이 될 때까지 반복
    while scoville[0] < K:
        # 더 이상 섞을 수 없을 때
        if len(scoville) < 2:
            return -1
        
        # 가장 작은 두 음식을 꺼내어 섞기
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_food = first + (second * 2)
        
        # 섞은 음식 다시 힙에 넣기
        heapq.heappush(scoville, new_food)
        mix_count += 1
    
    return mix_count
