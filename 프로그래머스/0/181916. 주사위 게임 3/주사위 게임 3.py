from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    cnt = Counter(dice)              # 예: {2: 3, 1: 1}
    freq = sorted(cnt.values(), reverse=True)  # 예: [3, 1]

    # 1) 네 주사위 숫자가 모두 같을 때
    if freq == [4]:
        p = dice[0]                  # 네 개 다 같으니까 아무거나
        return 1111 * p

    # 2) 세 개가 같고 하나만 다를 때 (3,1)
    if freq == [3, 1]:
        # count가 3인 숫자 p, 1인 숫자 q 찾기
        p = [num for num, c in cnt.items() if c == 3][0]
        q = [num for num, c in cnt.items() if c == 1][0]
        return (10 * p + q) ** 2

    # 3) 두 개씩 같은 값이 나왔을 때 (2,2)
    if freq == [2, 2]:
        nums = [num for num, c in cnt.items() if c == 2]
        p, q = nums[0], nums[1]
        return (p + q) * abs(p - q)

    # 4) 하나는 두 번, 나머지 둘은 각각 한 번 (2,1,1)
    if freq == [2, 1, 1]:
        p = [num for num, c in cnt.items() if c == 2][0]      # 필요 없지만 형식상
        others = [num for num, c in cnt.items() if c == 1]
        q, r = others[0], others[1]
        return q * r

    # 5) 전부 다 다른 경우 (1,1,1,1)
    # freq == [1,1,1,1]
    return min(dice)
