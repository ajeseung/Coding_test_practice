def solution(numbers, target):
    # DFS를 사용하여 탐색하는 함수 정의
    def dfs(index, current_sum):
        # 모든 숫자를 처리한 경우
        if index == len(numbers):
            # 현재 합계가 target과 같으면 1을 반환
            return 1 if current_sum == target else 0
        
        # 현재 숫자를 더하거나 빼는 두 가지 경우로 재귀 호출
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])
    
    # DFS 탐색 시작
    return dfs(0, 0)

