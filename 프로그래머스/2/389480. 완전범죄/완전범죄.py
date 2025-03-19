def solution(info, n, m):
    from functools import lru_cache
    
    def dfs(index, a_trace, b_trace):
        # 경찰에 걸리면 중단
        if a_trace >= n or b_trace >= m:
            return float('inf')
        
        # 모든 물건을 처리했을 때 A의 흔적 반환
        if index == len(info):
            return a_trace
        
        # 이미 방문한 상태는 최소값 유지하도록 메모이제이션
        if (index, a_trace, b_trace) in memo:
            return memo[(index, a_trace, b_trace)]
        
        # 현재 물건을 A가 가져갈 때와 B가 가져갈 때 비교
        a_choice = dfs(index + 1, a_trace + info[index][0], b_trace)
        b_choice = dfs(index + 1, a_trace, b_trace + info[index][1])
        
        # 최소 흔적 선택
        memo[(index, a_trace, b_trace)] = min(a_choice, b_choice)
        return memo[(index, a_trace, b_trace)]
    
    memo = {}
    result = dfs(0, 0, 0)
    return result if result != float('inf') else -1