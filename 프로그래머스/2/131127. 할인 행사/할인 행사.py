from collections import Counter

def solution(want, number, discount):
    need = dict(zip(want, number))
    n = len(discount)
    if n < 10:
        return 0

    window = Counter(discount[:10])

    def ok():
        # 모든 원하는 품목이 필요 수량 이상인지 확인
        for item, cnt in need.items():
            if window.get(item, 0) < cnt:
                return False
        return True

    ans = 0
    if ok():
        ans += 1

    for i in range(10, n):
        out_item = discount[i - 10]
        in_item = discount[i]

        # 윈도우에서 제거
        window[out_item] -= 1
        if window[out_item] == 0:
            del window[out_item]

        # 윈도우에 추가
        window[in_item] += 1

        if ok():
            ans += 1

    return ans
