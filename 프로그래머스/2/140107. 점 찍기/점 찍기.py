import math

def solution(k, d):
    answer = 0
    d2 = d * d
    
    # x를 0, k, 2k, ... , d 까지 움직인다
    for x in range(0, d + 1, k):
        # x^2 + y^2 <= d^2  →  y^2 <= d^2 - x^2
        max_y_sq = d2 - x * x
        max_y = int(math.isqrt(max_y_sq))   # 정수 제곱근
        
        # y = 0, k, 2k, ... <= max_y 인 y의 개수
        answer += max_y // k + 1
    
    return answer
