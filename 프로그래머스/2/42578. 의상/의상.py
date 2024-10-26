def solution(clothes):
    # 1. 종류별로 의상을 카운트할 딕셔너리 생성
    clothes_dict = {}
    
    # 2. 의상 종류별로 의상의 수를 카운트
    for item, kind in clothes:
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1

    # 3. 각 종류별로 (의상 수 + 1)을 모두 곱하고, 마지막에 아무것도 입지 않는 경우를 뺌
    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)

    # 4. 아무것도 입지 않는 경우를 제외하기 위해 최종 결과에서 1을 뺌
    return answer - 1
