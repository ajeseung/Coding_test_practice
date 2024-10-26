def time_to_seconds(time_str):
    """mm:ss 형식의 시간을 초 단위로 변환하는 함수"""
    minutes, seconds = map(int, time_str.split(":"))
    return minutes * 60 + seconds

def seconds_to_time(seconds):
    """초 단위 시간을 mm:ss 형식으로 변환하는 함수"""
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def solution(video_len, pos, op_start, op_end, commands):
    # 시간을 초로 변환
    video_len_sec = time_to_seconds(video_len)
    current_pos_sec = time_to_seconds(pos)
    op_start_sec = time_to_seconds(op_start)
    op_end_sec = time_to_seconds(op_end)
    
    # 명령 처리
    for command in commands:
                # 오프닝 건너뛰기 기능
        if op_start_sec <= current_pos_sec <= op_end_sec:
            current_pos_sec = op_end_sec
        if command == "prev":
            current_pos_sec = max(0, current_pos_sec - 10)
        elif command == "next":
            current_pos_sec = min(video_len_sec, current_pos_sec + 10)
        if op_start_sec <= current_pos_sec <= op_end_sec:
            current_pos_sec = op_end_sec

    
    # 최종 위치를 mm:ss 형식으로 변환하여 반환
    return seconds_to_time(current_pos_sec)
