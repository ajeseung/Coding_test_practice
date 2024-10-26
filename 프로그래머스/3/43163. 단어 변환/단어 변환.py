from collections import deque

def is_one_char_diff(word1, word2):
    # 두 단어의 차이가 하나의 문자만 다른지 확인하는 함수
    diff_count = sum([word1[i] != word2[i] for i in range(len(word1))])
    return diff_count == 1

def solution(begin, target, words):
    if target not in words:
        return 0  # target이 단어 목록에 없으면 변환할 수 없음
    
    # BFS 준비
    queue = deque([(begin, 0)])  # (현재 단어, 변환 횟수)
    visited = set()  # 방문한 단어를 기록
    
    while queue:
        current_word, depth = queue.popleft()
        
        # 목표 단어에 도달하면 변환 횟수 반환
        if current_word == target:
            return depth
        
        # 변환할 수 있는 단어들을 찾아서 큐에 추가
        for word in words:
            if word not in visited and is_one_char_diff(current_word, word):
                visited.add(word)
                queue.append((word, depth + 1))
    
    # 변환할 수 없는 경우
    return 0
