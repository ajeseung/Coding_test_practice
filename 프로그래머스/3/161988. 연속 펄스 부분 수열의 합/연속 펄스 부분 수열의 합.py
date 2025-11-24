def solution(sequence):
    INF = float('inf')
    
    max1 = -INF
    max2 = -INF
    
    cur1 = 0
    cur2 = 0
    
    for i, x in enumerate(sequence):
        p1 = x if i % 2 == 0 else -x
        p2 = -x if i % 2 == 0 else x
        
        cur1 = max(p1, p1 + cur1)
        cur2 = max(p2, p2 + cur2)
        
        max1 = max(cur1, max1)
        max2 = max(cur2, max2)
        
    return max(max1, max2)