def solution(book_time):
    # 시간을 분으로 변환하는 함수
    def time_to_minutes(time_str):
        h, m = map(int, time_str.split(":"))
        return h * 60 + m

    # 시작 시간과 종료 시간을 분 단위로 변환
    start_times = []
    end_times = []
    
    for start, end in book_time:
        start_times.append(time_to_minutes(start))
        end_times.append(time_to_minutes(end) + 10)  # 퇴실 후 청소 10분 추가

    # 시작 시간과 종료 시간을 정렬
    start_times.sort()
    end_times.sort()

    # 최소 객실 수 계산
    rooms = 0
    max_rooms = 0
    s_ptr, e_ptr = 0, 0

    while s_ptr < len(book_time):
        if start_times[s_ptr] < end_times[e_ptr]:  # 새로운 고객 입실
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            s_ptr += 1
        else:  # 기존 고객 퇴실 (청소 포함)
            rooms -= 1
            e_ptr += 1

    return max_rooms