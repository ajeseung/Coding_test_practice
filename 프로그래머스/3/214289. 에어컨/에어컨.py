def solution(temperature, t1, t2, a, b, onboard):
    MIN_TEMP = -10
    MAX_TEMP = 40
    SHIFT = 10
    INF = 10**15

    L = len(onboard)

    # dp[0]: 0분 시점
    prev = [INF] * (MAX_TEMP - MIN_TEMP + 1)
    prev[temperature + SHIFT] = 0  # 초기 실내온도 = 실외온도

    # 매 분 t -> t+1
    for t in range(L - 1):
        curr = [INF] * (MAX_TEMP - MIN_TEMP + 1)

        for k in range(MAX_TEMP - MIN_TEMP + 1):
            if prev[k] == INF:
                continue
            T = k - SHIFT  # 실제 온도

            # 현재 시점 온도도 탑승 시 쾌적 온도여야 함
            # (onboard[t]에 대한 체크; t=0은 0이라 상관 없음)
            if onboard[t] == 1 and not (t1 <= T <= t2):
                continue

            base_cost = prev[k]

            # 1) 에어컨 OFF: 실외온도로 1도 이동
            if T < temperature:
                T_off = T + 1
            elif T > temperature:
                T_off = T - 1
            else:
                T_off = T

            nk = T_off + SHIFT
            if MIN_TEMP <= T_off <= MAX_TEMP:
                if onboard[t + 1] == 0 or (t1 <= T_off <= t2):
                    curr[nk] = min(curr[nk], base_cost + 0)

            # 2) 에어컨 ON, 유지 (비용 b)
            T_same = T
            nk = T_same + SHIFT
            if MIN_TEMP <= T_same <= MAX_TEMP:
                if onboard[t + 1] == 0 or (t1 <= T_same <= t2):
                    curr[nk] = min(curr[nk], base_cost + b)

            # 3) 에어컨 ON, 온도 올리기 (비용 a)
            if T < MAX_TEMP:
                T_up = T + 1
                nk = T_up + SHIFT
                if onboard[t + 1] == 0 or (t1 <= T_up <= t2):
                    curr[nk] = min(curr[nk], base_cost + a)

            # 4) 에어컨 ON, 온도 내리기 (비용 a)
            if T > MIN_TEMP:
                T_down = T - 1
                nk = T_down + SHIFT
                if onboard[t + 1] == 0 or (t1 <= T_down <= t2):
                    curr[nk] = min(curr[nk], base_cost + a)

        prev = curr  # 다음 분으로 이동

    # 마지막 시점(L-1분)에서도 탑승 중이면 쾌적 온도만 남아 있음
    answer = min(prev)
    return answer
