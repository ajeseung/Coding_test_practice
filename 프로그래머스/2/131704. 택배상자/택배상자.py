def solution(order):
    stack = []
    box = 1              # 메인 벨트에서 꺼낼 다음 박스 번호
    idx = 0              # order에서 현재 실어야 할 위치
    n = len(order)

    while True:
        # 1. 메인 벨트에서 아직 꺼낼 박스가 있고,
        #    바로 싣거나 보조에 넣을 수 있는 동안 진행
        if box <= n:
            if box == order[idx]:
                # 바로 트럭에 싣기
                idx += 1
                box += 1
            else:
                # 보조 벨트(스택)에 넣기
                stack.append(box)
                box += 1
        else:
            # 메인 벨트는 끝났다면 보조 벨트만 체크
            if stack and stack[-1] == order[idx]:
                stack.pop()
                idx += 1
            else:
                break

        # 메인에서 하나 처리한 후, 보조 벨트에서도 가능한 만큼 싣기
        while stack and idx < n and stack[-1] == order[idx]:
            stack.pop()
            idx += 1

        if idx >= n:
            break

    return idx
