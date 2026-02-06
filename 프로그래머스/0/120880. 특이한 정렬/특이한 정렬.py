def solution(numlist, n):
    def custom(x):
        return (abs(x-n), -x)
    
    return sorted(numlist, key=custom)
