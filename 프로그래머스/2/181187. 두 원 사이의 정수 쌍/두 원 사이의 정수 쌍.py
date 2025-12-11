from math import isqrt

def solution(r1, r2):
    total = 0
    
    # x >= 1, y >= 1 인 1사분면의 점만 센다.
    for x in range(1, r2 + 1):
        # 바깥 원에서 가능한 y의 최대값 (정수)
        maxY2 = r2 * r2 - x * x
        if maxY2 < 1:      # y^2 <= maxY2인데 1^2=1도 안 들어가면 y>=1 정수 해 없음
            continue
        maxY = isqrt(maxY2)   # floor(sqrt(maxY2))
        
        # 안쪽 원에서 가능한 y의 최소값 (정수, y>=1 기준)
        if x >= r1:
            # x^2 >= r1^2 이면 y=0부터 이미 안쪽 원 안에 있으니,
            # y>=1일 때 최소 y는 1
            minY = 1
        else:
            # r1^2 - x^2 > 0 인 경우: y^2 >= r1^2 - x^2
            # y >= ceil(sqrt(r1^2 - x^2))
            minY2 = r1 * r1 - x * x
            # ceil(sqrt(n)) = floor(sqrt(n-1)) + 1   (n > 0일 때)
            minY = isqrt(minY2 - 1) + 1
            if minY < 1:
                minY = 1
        
        if maxY >= minY:
            total += (maxY - minY + 1)
    
    # total: 1사분면에서 x>=1, y>=1인 점들의 개수
    # 네 방향 대칭 → ×4
    answer = total * 4
    
    # 축 위의 점들 (x=0 또는 y=0)
    answer += 4 * (r2 - r1 + 1)
    
    return answer
