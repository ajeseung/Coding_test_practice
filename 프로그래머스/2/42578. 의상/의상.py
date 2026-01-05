
from collections import Counter

def solution(clothes):
    cnt = Counter(kind for name, kind in clothes)
    ans = 1
    
    for c in cnt.values():
        ans *= (c+1)
    
    return ans-1
    













