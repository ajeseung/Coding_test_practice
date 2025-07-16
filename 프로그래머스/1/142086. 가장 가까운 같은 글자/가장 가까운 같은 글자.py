def solution(s):
    last_seen = {}  # 각 문자의 마지막 인덱스를 저장
    result = []

    for i, char in enumerate(s):
        if char in last_seen:
            result.append(i - last_seen[char])
        else:
            result.append(-1)
        last_seen[char] = i  # 현재 문자의 위치를 기록

    return result
