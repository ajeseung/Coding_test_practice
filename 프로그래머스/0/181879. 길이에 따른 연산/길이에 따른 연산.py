import math

def solution(num_list):
    answer = 0
    n = len(num_list)
    
    if n >= 11:
        return sum(num_list)
    else:
        return math.prod(num_list)