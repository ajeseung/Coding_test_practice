def solution(n):
    # 계단형(삼각형) 2차원 리스트 만들기: 1행 1칸, 2행 2칸, ... n행 n칸
    tri = [[0] * (i + 1) for i in range(n)]
    
    num = 1               # 채울 숫자
    x, y = -1, 0          # 현재 위치(다음 이동을 위해 x를 -1에서 시작)
    
    # i번째 바퀴: i % 3에 따라 방향이 (아래 → 오른쪽 → 왼쪽 위)로 반복
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:        # 아래로 이동
                x += 1
            elif i % 3 == 1:      # 오른쪽으로 이동
                y += 1
            else:                 # 왼쪽 위로 이동
                x -= 1
                y -= 1
            tri[x][y] = num
            num += 1

    # 행 순서대로 1차원 배열로 펼치기
    answer = []
    for row in tri:
        answer.extend(row)
    return answer
