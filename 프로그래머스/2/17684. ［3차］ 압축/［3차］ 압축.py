def solution(msg):
    # 1. 사전 초기화 (A~Z)
    dic = {}
    for i in range(26):
        dic[chr(ord('A') + i)] = i + 1
    next_index = 27

    answer = []
    i = 0
    n = len(msg)

    while i < n:
        # 2. 가장 긴 w 찾기
        j = i + 1
        while j <= n and msg[i:j] in dic:
            j += 1

        # 루프가 끝나면 msg[i:j]는 사전에 없음 (혹은 j == n+1)
        # 따라서 가장 긴 w는 msg[i:j-1]
        w = msg[i:j-1]
        answer.append(dic[w])

        # 3. 다음 글자 c가 있으면 w + c 사전에 추가
        if j <= n:
            c = msg[j-1]
            new_word = w + c
            if new_word not in dic:
                dic[new_word] = next_index
                next_index += 1

        # 4. i를 w 길이만큼 이동
        i += len(w)

    return answer
