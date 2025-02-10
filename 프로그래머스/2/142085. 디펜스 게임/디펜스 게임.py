import heapq

def solution(n, k, enemy):
    max_heap = []
    rounds = 0
    
    for e in enemy:
        heapq.heappush(max_heap,-e)
        n -= e
        
        if n < 0:
            if k > 0:
                n += -heapq.heappop(max_heap)
                k -= 1
            else:
                break
        rounds += 1
    
    return rounds