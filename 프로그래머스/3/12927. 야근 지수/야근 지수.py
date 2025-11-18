import heapq

def solution(n, works):
    # 1. 전부 다 처리 가능하면 0 리턴
    total = sum(works)
    if total <= n:
        return 0

    # 2. 파이썬 heapq는 최소 힙이라서, 음수로 바꿔서 최대 힙처럼 사용
    #    ex) 작업량 4,3,3 -> -4,-3,-3
    heap = []
    for w in works:
        heapq.heappush(heap, -w)

    # 3. n시간 동안 가장 큰 값부터 1씩 줄이기
    for _ in range(n):
        # 현재 가장 큰 작업량 (음수로 들어있으니까 다시 양수로)
        max_work = -heapq.heappop(heap)

        if max_work == 0:   # 더 줄일 일이 없으면 끝
            heapq.heappush(heap, 0)
            break

        max_work -= 1       # 1시간 일했으니까 작업량 1 감소
        heapq.heappush(heap, -max_work)

    # 4. 남은 작업량들의 제곱 합 계산
    answer = 0
    while heap:
        w = -heapq.heappop(heap)
        answer += w * w

    return answer
