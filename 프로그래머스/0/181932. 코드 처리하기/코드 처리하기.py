def solution(code):
    mode = 0           # 시작은 0
    ret = []           # 문자열 누적은 리스트로 (성능)

    for idx, ch in enumerate(code):
        if ch == "1":          # 토글 문자면 모드 전환
            mode = 1 - mode    # 또는 mode ^= 1
            continue

        if mode == 0:
            if idx % 2 == 0:   # 짝수 인덱스만 추가
                ret.append(ch)
        else:  # mode == 1
            if idx % 2 == 1:   # 홀수 인덱스만 추가
                ret.append(ch)

    ans = "".join(ret)
    return ans if ans else "EMPTY"
