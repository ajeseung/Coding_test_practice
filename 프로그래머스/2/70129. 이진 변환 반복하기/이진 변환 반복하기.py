def solution(s):
    count = 0         # 변환 횟수
    zero_count = 0    # 제거한 0의 개수 누적

    while s != '1':
        zeros = s.count('0')         # 이번 회차에서 제거할 0의 개수
        zero_count += zeros          # 누적
        s = s.replace('0', '')       # 0 제거
        s = bin(len(s))[2:]          # 남은 길이를 2진수 문자열로 변환
        count += 1                   # 변환 횟수 증가

    return [count, zero_count]
