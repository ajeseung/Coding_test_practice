def solution(numbers):
    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 문자열을 기준으로, 두 개의 문자열을 붙여 비교한 결과로 내림차순 정렬
    numbers.sort(reverse=True, key=lambda x: x*5)
    
    # 정렬된 숫자를 이어붙임
    answer = ''.join(numbers)
    
    # '0000' 같은 경우는 '0'으로 반환
    if answer[0] == '0':
        return '0'
    
    return answer
