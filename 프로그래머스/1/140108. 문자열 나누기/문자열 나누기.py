def solution(s):
    count = 0
    i = 0

    while i < len(s):
        x = s[i]
        x_count = 0
        other_count = 0

        for j in range(i, len(s)):
            if s[j] == x:
                x_count += 1
            else:
                other_count += 1

            if x_count == other_count:
                break

        count += 1
        i = j + 1  # 다음 분리 시작 지점으로 이동

    return count