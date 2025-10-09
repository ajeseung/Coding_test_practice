from collections import defaultdict

def solution(edges):
    indeg = defaultdict(int)
    outdeg = defaultdict(int)
    nodes = set()

    for a, b in edges:
        outdeg[a] += 1
        indeg[b] += 1
        nodes.add(a); nodes.add(b)

    # 1) 생성한 정점 g 찾기: in=0 and out>=2
    g = -1
    for v in nodes:
        if indeg[v] == 0 and outdeg[v] >= 2:
            g = v
            break

    total = outdeg[g]  # 그래프 개수의 합

    # 2) 막대 개수: out=0인 정점 수 (g 제외)
    sticks = sum(1 for v in nodes if v != g and outdeg[v] == 0)

    # 3) 8자 개수: out=2인 정점 수 (g 제외)
    eights = sum(1 for v in nodes if v != g and outdeg[v] == 2)

    # 4) 도넛 개수: 전체 - 막대 - 8자
    donuts = total - sticks - eights

    return [g, donuts, sticks, eights]
