from collections import deque

def solution(x, y, n):
    # BFS를 위한 큐 (현재 숫자, 연산 횟수)
    queue = deque([(x, 0)])
    visited = set([x])  # 방문한 숫자 저장
    
    while queue:
        num, count = queue.popleft()
        
        # 목표 값 도달 시 최소 연산 횟수 반환
        if num == y:
            return count

        # 가능한 연산 수행
        for next_num in (num + n, num * 2, num * 3):
            if next_num <= y and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, count + 1))

    # 변환 불가능할 경우 -1 반환
    return -1