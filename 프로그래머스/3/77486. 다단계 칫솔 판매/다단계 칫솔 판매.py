def solution(enroll, referral, seller, amount):
    idx = {name: i for i, name in enumerate(enroll)}
    
    parent = {}
    
    for e,r in zip(enroll, referral):
        parent[e] = r
        
    profit = [0] * len(enroll)
    
    for name, cnt in zip(seller, amount):
        money = cnt * 100
        cur = name
        
        while cur != "-" and money > 0:
            give = money // 10
            keep = money - give
        
            profit[idx[cur]] += keep
            
            cur = parent[cur]
            money = give
            
    return profit