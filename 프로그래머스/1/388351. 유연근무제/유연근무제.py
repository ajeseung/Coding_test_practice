def add_10_minutes(t):
    # t는 HHMM 형식의 정수 (예: 730, 958)
    h = t // 100
    m = t % 100

    m += 10
    if m >= 60:
        h += 1
        m -= 60

    return h * 100 + m


def solution(schedules, timelogs, startday):
    n = len(schedules)
    answer = 0

    # timelogs[i][j]에서 j(0~6)가 평일인지 판별해야 함
    # startday = 이벤트 1일차의 요일 (1=월, ..., 7=일)
    # j일차의 실제 요일: ((startday - 1) + j) % 7 + 1
    weekdays = []
    for j in range(7):  # j = 0 ~ 6 (이벤트 1~7일차)
        dayofweek = ((startday - 1) + j) % 7 + 1  # 1~7
        if 1 <= dayofweek <= 5:   # 월~금만 평일
            weekdays.append(j)    # timelogs 인덱스는 j 그대로 사용

    for i in range(n):  # 각 직원에 대해
        # 출근 인정 마감 시간 = 희망 시각 + 10분
        limit = add_10_minutes(schedules[i])
        ok = True

        # 해당 직원의 평일 출근 기록만 확인
        for day in weekdays:
            if timelogs[i][day] > limit:  # 한 번이라도 지각이면 탈락
                ok = False
                break

        if ok:
            answer += 1

    return answer
