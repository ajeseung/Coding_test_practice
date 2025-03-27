def solution(numbers):
    m = sum(set(range(10)) - set(numbers))
    print(m)
    
    return m