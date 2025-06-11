import math
from collections import defaultdict

def time_to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    in_time = dict()
    total_time = defaultdict(int)

    for record in records:
        time, car, status = record.split()
        minutes = time_to_minutes(time)

        if status == 'IN':
            in_time[car] = minutes
        else:  # 'OUT'
            duration = minutes - in_time[car]
            total_time[car] += duration
            del in_time[car]

    # 출차 기록 없는 차량 처리
    for car, minutes in in_time.items():
        total_time[car] += time_to_minutes("23:59") - minutes

    # 요금 계산
    result = []
    for car in sorted(total_time):
        time = total_time[car]
        if time <= base_time:
            fee = base_fee
        else:
            extra = math.ceil((time - base_time) / unit_time)
            fee = base_fee + extra * unit_fee
        result.append(fee)

    return result
