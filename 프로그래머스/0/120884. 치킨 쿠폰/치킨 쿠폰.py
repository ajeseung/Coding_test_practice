def solution(chicken):
    coupon = chicken
    service = 0
    
    while coupon >= 10:
        new = coupon // 10       # 새로 받을 치킨
        service += new
        
        coupon = coupon % 10     # 남은 쿠폰
        coupon += new            # 서비스 치킨에서 나온 쿠폰
        
    return service
