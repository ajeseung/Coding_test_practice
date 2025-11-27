def solution(a):
    n = len(a)
    if n <= 2:
        # 풍선이 1개나 2개면 어차피 둘 다(또는 하나) 다 살릴 수 있음
        return n

    # 1. 오른쪽 최소값 배열 (suffix min)
    right_min = [0] * n
    right_min[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(a[i], right_min[i + 1])

    # 2. 왼쪽 최소값을 한 변수로만 관리
    left_min = float('inf')
    answer = 0

    for i in range(n):
        # 오른쪽 최소값은 i+1부터 보므로, 마지막은 없다고 보고 +∞ 취급
        if i == n - 1:
            rmin = float('inf')
        else:
            rmin = right_min[i + 1]

        # 3. 둘 중 하나라도 만족하면 이 풍선은 끝까지 생존 가능
        if a[i] <= left_min or a[i] <= rmin:
            answer += 1

        # 현재 풍선을 포함해 왼쪽 최소값 갱신
        if a[i] < left_min:
            left_min = a[i]

    return answer
