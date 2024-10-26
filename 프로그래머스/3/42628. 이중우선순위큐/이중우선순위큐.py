import heapq

def solution(operations):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙 (음수로 저장하여 최대 힙을 구현)
    entry_finder = {}  # 삽입된 값을 기록하는 딕셔너리로, 동기화 처리를 위해 사용
    
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        
        if op == 'I':  # 삽입 연산
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            if num in entry_finder:
                entry_finder[num] += 1
            else:
                entry_finder[num] = 1
        
        elif op == 'D':  # 삭제 연산
            if num == 1:  # 최댓값 삭제
                while max_heap and entry_finder[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)  # 동기화: 이미 삭제된 값이 남아있다면 제거
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    entry_finder[max_val] -= 1
            elif num == -1:  # 최솟값 삭제
                while min_heap and entry_finder[min_heap[0]] == 0:
                    heapq.heappop(min_heap)  # 동기화: 이미 삭제된 값이 남아있다면 제거
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    entry_finder[min_val] -= 1
    
    # 최종 동기화: 최소 힙과 최대 힙에서 남아 있는 쓰레기 값 제거
    while min_heap and entry_finder[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and entry_finder[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    
    if not min_heap or not max_heap:
        return [0, 0]
    
    return [-max_heap[0], min_heap[0]]
