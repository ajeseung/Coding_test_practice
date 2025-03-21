def solution(n, l, r):
    # 5^n 길이
    total_length = pow(5, n)

    def count_ones(n, l, r, start=1, end=None):
        if end is None:
            end = pow(5, n)

        # 겹치지 않는 경우
        if r < start or end < l:
            return 0

        # n == 0이면 비트열은 '1'
        if n == 0:
            return 1

        # 현재 범위를 5등분
        length = (end - start + 1) // 5
        result = 0
        for i in range(5):
            new_start = start + i * length
            new_end = new_start + length - 1
            # 0이 되는 구간은 i == 2
            if i == 2:
                continue
            result += count_ones(n - 1, l, r, new_start, new_end)

        return result

    return count_ones(n, l, r)
