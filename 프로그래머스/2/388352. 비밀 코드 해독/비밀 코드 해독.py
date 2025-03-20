from itertools import combinations

def solution(n, q, ans):
    all_combinations = list(combinations(range(1, n + 1), 5))  # 모든 가능한 5개 조합 생성
    valid_count = 0  # 조건을 만족하는 조합의 개수
    
    for secret_code in all_combinations:
        valid = True
        
        for i in range(len(q)):
            query_set = set(q[i])
            secret_set = set(secret_code)
            common_count = len(query_set & secret_set)  # 교집합 개수 계산
            
            if common_count != ans[i]:  # 주어진 ans[i] 값과 다르면 제외
                valid = False
                break
        
        if valid:
            valid_count += 1  # 유효한 조합 개수 증가
    
    return valid_count
