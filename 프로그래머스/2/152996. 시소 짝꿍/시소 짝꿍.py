from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    ratios = [(1,1), (2,3), (2,4), (3,2), (3,4), (4,2), (4,3)]
    
    for w in counter:
        for r1, r2 in ratios:
            target = w * r1 / r2
            if target != int(target):
                continue
                
            target = int(target)
            if target not in counter:
                continue
                
            if w == target:
                answer += counter[w] * (counter[w] -1) // 2
                
            elif w < target:
                answer += counter[w] * counter[target]
                
    return answer