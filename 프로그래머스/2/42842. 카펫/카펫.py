def solution(brown, yellow):
    total = brown + yellow  # 전체 격자의 수
    
    # 1. 가능한 세로 길이를 찾기 (세로 길이는 3부터 시작)
    for height in range(3, total + 1):
        if total % height == 0:  # 가로 길이가 정수로 나눠떨어질 때
            width = total // height  # 가로 길이를 계산
            
            # 2. 조건을 만족하는지 확인
            if (width - 2) * (height - 2) == yellow:
                return [width, height]  # 가로 길이가 세로보다 크거나 같으므로 반환


            