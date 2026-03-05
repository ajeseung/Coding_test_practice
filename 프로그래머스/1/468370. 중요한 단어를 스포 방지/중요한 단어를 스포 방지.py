def solution(message, spoiler_ranges):
    # 1) 단어 파싱: (word, start, end)
    words = []
    n = len(message)
    i = 0
    while i < n:
        if message[i] == ' ':
            i += 1
            continue
        s = i
        while i < n and message[i] != ' ':
            i += 1
        e = i - 1
        words.append((message[s:i], s, e))

    m = len(spoiler_ranges)

    # 2) 각 단어가 어떤 스포 구간들과 겹치는지(단어-스포 overlap) 투포인터로 계산
    #    - 스포가 하나도 안 겹치면 '평문 단어'로 기록
    visible_nonspoiler_words = set()  # 스포가 전혀 걸리지 않은(평문) 단어 문자열
    reveal_groups = [[] for _ in range(m)]  # reveal_groups[k] = k번째 스포 클릭 시 완전공개되는 단어들 (word, start)

    r = 0  # spoiler_ranges pointer
    for w, ws, we in words:
        # 현재 단어 시작보다 완전히 왼쪽에 끝난 스포 구간들은 넘김
        while r < m and spoiler_ranges[r][1] < ws:
            r += 1

        j = r
        last_overlap = -1
        # 단어 구간과 겹치는 스포 구간들을 모두 찾음
        while j < m and spoiler_ranges[j][0] <= we:
            s, e = spoiler_ranges[j]
            # 실제 겹침 체크 (공백은 단어구간 밖이므로 ws~we 교집합만 보면 됨)
            if not (e < ws or we < s):
                last_overlap = j
            j += 1

        if last_overlap == -1:
            # 스포가 전혀 안 걸린 단어(평문)
            visible_nonspoiler_words.add(w)
        else:
            # 마지막으로 겹치는 스포 구간을 클릭하는 순간 완전 공개
            reveal_groups[last_overlap].append((w, ws))

    # 3) 클릭 순서대로 처리하면서 "중요 단어" 세기
    revealed_spoiler_words = set()  # 이전에 완전히 공개된 스포 단어 문자열
    important_count = 0

    for k in range(m):
        group = reveal_groups[k]
        if not group:
            continue
        # 같은 클릭에서 동시에 공개된 단어는 왼->오 순서로 판정
        group.sort(key=lambda x: x[1])  # start index 기준

        for w, _ in group:
            # 중요 단어 조건:
            # - 평문 구간에서 등장한 적 없어야 함
            # - 이전에 공개된 스포 단어와 중복 아니어야 함
            if (w not in visible_nonspoiler_words) and (w not in revealed_spoiler_words):
                important_count += 1
            # 공개된 스포 단어로 기록 (중요 여부와 무관)
            revealed_spoiler_words.add(w)

    return important_count