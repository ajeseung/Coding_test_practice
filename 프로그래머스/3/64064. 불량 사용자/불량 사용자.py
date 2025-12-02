def match(user, banned):
    # user_id와 banned_id가 패턴 매칭되는지 확인
    if len(user) != len(banned):
        return False
    for u, b in zip(user, banned):
        if b == '*':
            continue
        if u != b:
            return False
    return True

def solution(user_id, banned_id):
    result = set()  # frozenset으로 된 제재 아이디 조합들을 저장

    n = len(banned_id)

    def dfs(idx, used):
        # idx: 현재 처리 중인 banned_id 인덱스
        if idx == n:
            # 하나의 경우 완료 → frozenset으로 만들어 set에 추가
            result.add(frozenset(used))
            return

        pattern = banned_id[idx]
        for user in user_id:
            if user in used:
                continue
            if not match(user, pattern):
                continue

            # 이 user를 현재 banned에 매칭
            used.add(user)
            dfs(idx + 1, used)
            used.remove(user)

    dfs(0, set())

    return len(result)
