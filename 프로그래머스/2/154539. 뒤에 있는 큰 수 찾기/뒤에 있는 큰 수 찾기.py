def solution(numbers):
    n = len(numbers)
    answer = [-1] * n  # 결과를 저장할 배열, 초기값은 모두 -1
    stack = []  # 스택을 사용하여 뒷 큰수를 저장
    
    for i in range(n - 1, -1, -1):  # 배열을 뒤에서부터 탐색
        # 스택의 맨 위가 현재 숫자보다 작으면 제거
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        
        # 스택이 비어 있지 않으면, 스택의 맨 위가 뒷 큰수
        if stack:
            answer[i] = stack[-1]
        
        # 현재 숫자를 스택에 추가
        stack.append(numbers[i])
    
    return answer

# 예시 테스트 실행
numbers1 = [2, 3, 3, 5]
numbers2 = [9, 1, 5, 3, 6, 2]

print(solution(numbers1))  # [3, 5, 5, -1]
print(solution(numbers2))  # [-1, 5, 6, 6, -1, -1]
