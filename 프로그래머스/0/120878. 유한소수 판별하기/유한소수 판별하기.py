import math

def solution(a, b):
    # 1. 기약분수 만들기
    g = math.gcd(a, b)
    b //= g
    
    # 2. 분모에서 2 제거
    while b % 2 == 0:
        b //= 2
        
    # 3. 분모에서 5 제거
    while b % 5 == 0:
        b //= 5
    
    # 4. 판단
    return 1 if b == 1 else 2
