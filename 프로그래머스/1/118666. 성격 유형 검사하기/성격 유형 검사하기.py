def solution(survey, choices):
    # 1. 점수 테이블 초기화
    scores = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0,
    }

    # 2. 각 문항에 대해 점수 누적
    for s, c in zip(survey, choices):
        disagree = s[0]  # 비동의 쪽 성격 유형
        agree = s[1]     # 동의 쪽 성격 유형

        if c < 4:  # 비동의 쪽에 점수
            scores[disagree] += 4 - c   # 1→3, 2→2, 3→1
        elif c > 4:  # 동의 쪽에 점수
            scores[agree] += c - 4      # 5→1, 6→2, 7→3
        # c == 4면 아무 점수도 추가 안 함

    # 3. 각 지표별로 최종 성격 유형 선택
    result = []

    # 1번 지표: R vs T
    result.append('R' if scores['R'] >= scores['T'] else 'T')
    # 2번 지표: C vs F
    result.append('C' if scores['C'] >= scores['F'] else 'F')
    # 3번 지표: J vs M
    result.append('J' if scores['J'] >= scores['M'] else 'M')
    # 4번 지표: A vs N
    result.append('A' if scores['A'] >= scores['N'] else 'N')

    # 4. 문자열로 합쳐서 반환
    return ''.join(result)
