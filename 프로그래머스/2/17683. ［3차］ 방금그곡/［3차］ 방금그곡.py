def convert_melody(melody: str):
    replace_map = {
        "C#": "c",
        "D#": "d",
        "E#": "F",
        "F#": "f",
        "G#": "g",
        "A#": "a",
        "B#": "C"
    }
    for k,v in replace_map.items():
        melody = melody.replace(k,v)
    return melody

def time_to_min(t: str) -> int:
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solution(m, musicinfos):
    answer = "(None)"
    best_time = -1
    m_conv = convert_melody(m)
    
    for idx, info in enumerate(musicinfos):
        start, end, title, score = info.split(",")
        start_min = time_to_min(start)
        end_min = time_to_min(end)
        play_time = end_min - start_min

        score_conv = convert_melody(score)

        # 실제 재생된 멜로디 생성
        if len(score_conv) >= play_time:
            played = score_conv[:play_time]
        else:
            # 반복해서 play_time 길이만큼
            repeat = play_time // len(score_conv) + 1
            played = (score_conv * repeat)[:play_time]

        # 멜로디 포함 여부 확인
        if m_conv in played:
            # 더 긴 재생 시간이면 무조건 갱신
            # 재생 시간이 같으면 먼저 나온 곡을 그대로 두면 되므로,
            # 여기서는 '>' 만 사용
            if play_time > best_time:
                best_time = play_time
                answer = title

    return answer