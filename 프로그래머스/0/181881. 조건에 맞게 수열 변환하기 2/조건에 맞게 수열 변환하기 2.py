def solution(arr):
    def transform(x):
        # 규칙에 맞게 x를 한 번 변환
        if x >= 50 and x % 2 == 0:
            return x // 2
        elif x < 50 and x % 2 == 1:
            return x * 2 + 1
        else:
            return x

    x = 0  # 반복 횟수

    while True:
        changed = False
        new_arr = []

        for v in arr:
            nv = transform(v)
            new_arr.append(nv)
            if nv != v:
                changed = True

        if not changed:   # 이번 턴에 아무 것도 안 변했다 = arr(x) == arr(x+1)
            return x

        arr = new_arr
        x += 1
