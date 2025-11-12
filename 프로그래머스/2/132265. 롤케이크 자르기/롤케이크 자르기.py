from collections import Counter

def solution(topping):
    n = len(topping)
    
    if n < 2:
        return 0
    
    right = Counter(topping)
    right_cnt = len(right)
    
    left = set()
    left_cnt = 0
    
    cnt = 0
    
    for i in range(n-1):
        t = topping[i]
        
        if t not in left:
            left.add(t)
            left_cnt += 1
            
        right[t] -= 1
        if right[t] == 0:
            right_cnt -=1
            del right[t]
            
        if left_cnt == right_cnt:
            cnt +=1
            
    return cnt