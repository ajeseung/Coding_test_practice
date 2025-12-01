from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    # 1. 각 주문을 알파벳 오름차순으로 정렬
    orders = [''.join(sorted(order)) for order in orders]

    # 2. 각 코스 길이 별로 처리
    for c in course:
        combos = []

        # 2-1. 각 주문에서 길이 c짜리 조합 모두 뽑기
        for order in orders:
            if len(order) >= c:
                for comb in combinations(order, c):
                    combos.append(''.join(comb))  # ('A','C') -> "AC"

        # 해당 길이의 조합이 하나도 없으면 다음 코스로
        if not combos:
            continue

        # 2-2. 등장 횟수 세기
        counter = Counter(combos)
        max_count = max(counter.values())

        # 2명 이상이 주문한 조합만 코스로 인정
        if max_count < 2:
            continue

        # 2-3. 최대 빈도인 조합들만 골라서 answer에 추가
        for menu, cnt in counter.items():
            if cnt == max_count:
                answer.append(menu)

    # 3. 전체 결과를 사전 순으로 정렬
    return sorted(answer)
