def solution(quiz):
    ans = []
    for q in quiz:
        x, op, y, eq, z = q.split()   # eq는 항상 "="
        x, y, z = int(x), int(y), int(z)

        val = x + y if op == "+" else x - y
        ans.append("O" if val == z else "X")
    return ans
