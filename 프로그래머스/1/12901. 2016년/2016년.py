def solution(a, b):
    # 2016년은 윤년 → 2월 29일
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = b + sum(month_days[:a-1])  # 1월 1일이 day=1이라는 기준으로 누적

    # 2016-01-01 = FRI. day % 7 이 1일 때 FRI가 나오도록 배열을 이렇게 둡니다.
    names = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    return names[total % 7]
