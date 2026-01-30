def solution(name):
    n = len(name)

    # 1) 위/아래 조작 합
    up_down = 0
    for c in name:
        up = ord(c) - ord('A')
        down = ord('Z') - ord(c) + 1
        up_down += min(up, down)

    # 2) 좌/우 최소 이동
    move = n - 1  # 그냥 오른쪽으로만 가는 경우

    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        # 오른쪽 갔다가 되돌아오기 vs 왼쪽 먼저 갔다가 오기
        move = min(move,
                   2 * i + (n - next_idx),
                   i + 2 * (n - next_idx))

    return up_down + move
