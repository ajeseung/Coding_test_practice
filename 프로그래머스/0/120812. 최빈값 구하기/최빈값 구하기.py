from collections import Counter

def solution(array):
    cnt = Counter(array)
    most = cnt.most_common()
    
    if len(most) == 1:
        return most[0][0]
    
    if most[0][1] == most[1][1]:
        return -1
    
    return most[0][0]