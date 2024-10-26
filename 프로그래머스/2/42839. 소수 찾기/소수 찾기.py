# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 재귀적으로 순열 생성
def generate_permutations(current, remaining, all_combinations):
    if current != "":  # 빈 문자열이 아닌 경우 숫자로 변환하여 추가
        all_combinations.add(int(current))
    
    # 남은 숫자들이 있으면 재귀 호출
    for i in range(len(remaining)):
        generate_permutations(current + remaining[i], remaining[:i] + remaining[i+1:], all_combinations)

def solution(numbers):
    all_combinations = set()  # 중복된 숫자를 제거하기 위해 set 사용
    
    # 순열 생성 시작 (초기 current는 빈 문자열, remaining은 모든 숫자 조각)
    generate_permutations("", numbers, all_combinations)
    
    # 소수 판별 및 카운트
    prime_count = 0
    for num in all_combinations:
        if is_prime(num):
            prime_count += 1
    
    return prime_count

