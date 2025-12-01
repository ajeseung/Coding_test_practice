from collections import deque

def solution(queue1, queue2):
    # 1. 합 계산
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1 + sum2

    # total이 홀수면 불가능
    if total % 2 == 1:
        return -1

    target = total // 2

    # 혹시 하나가 target보다 큰 값이면 바로 불가능 (선택사항이지만 빠른 탈출용)
    if max(max(queue1), max(queue2)) > target:
        return -1

    # 큐를 deque로 두고, 인덱스 대신 실제 popleft/append로 시뮬레이션해도 됨.
    # 다만 pop(0) 대신 deque를 써야 O(1).
    q1 = deque(queue1)
    q2 = deque(queue2)

    limit = len(queue1) * 3  # 최대 연산 횟수 (경험적으로 충분)
    cnt = 0

    i = 0  # 인덱스 대신 cnt로도 충분히 제어 가능하지만, 여기서는 deque로 처리하자.

    # deque 버전: 투 포인터 대신 실제 이동 시뮬레이션
    while cnt <= limit:
        if sum1 == target:
            return cnt

        if sum1 > target:
            # q1 -> q2로 이동
            if not q1:  # 안전 체크
                return -1
            x = q1.popleft()
            sum1 -= x
            sum2 += x
            q2.append(x)
        else:
            # q2 -> q1로 이동
            if not q2:  # 안전 체크
                return -1
            x = q2.popleft()
            sum2 -= x
            sum1 += x
            q1.append(x)

        cnt += 1

    # 여기까지 오면 불가능
    return -1
