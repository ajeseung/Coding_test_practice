def solution(keymap, targets):
    # 각 문자가 최소 몇 번 눌러야 입력 가능한지 저장할 딕셔너리
    min_presses = {}

    # keymap을 순회하며 최소 누름 수 계산
    for i, keys in enumerate(keymap):
        for idx, char in enumerate(keys):
            # 현재 문자를 누르려면 (idx + 1)번 눌러야 함
            if char in min_presses:
                min_presses[char] = min(min_presses[char], idx + 1)
            else:
                min_presses[char] = idx + 1

    answer = []
    for target in targets:
        total_presses = 0
        for char in target:
            if char in min_presses:
                total_presses += min_presses[char]
            else:
                total_presses = -1
                break
        answer.append(total_presses)

    return answer