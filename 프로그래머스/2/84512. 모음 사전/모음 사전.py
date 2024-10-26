def solution(word):
    # 각 자리가 가지는 가중치
    weights = [781, 156, 31, 6, 1]  # 5^4, 5^3, 5^2, 5^1, 5^0
    vowels = ['A', 'E', 'I', 'O', 'U']  # 모음 리스트
    result = 0
    
    # 각 자리에서의 계산
    for i, ch in enumerate(word):
        result += vowels.index(ch) * weights[i] + 1  # 해당 문자에 대한 가중치 계산 후 더함
        
    return result
