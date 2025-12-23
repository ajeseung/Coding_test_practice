def solution(numbers):
    numbers.sort()
    # 가장 큰 두 수
    max1 = numbers[-1] * numbers[-2]
    # 가장 작은 두 수 (음수 두 개면 양수로 커질 수 있음)
    max2 = numbers[0] * numbers[1]
    return max(max1, max2)
