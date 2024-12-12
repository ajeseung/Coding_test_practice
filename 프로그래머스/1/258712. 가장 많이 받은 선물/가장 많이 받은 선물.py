from collections import defaultdict

def solution(friends, gifts):
    given = defaultdict(int)
    received = defaultdict(int)
    interactions = defaultdict(lambda: defaultdict(int))
    
    for gift in gifts:
        giver, receiver = gift.split()
        given[giver] += 1
        received[receiver] += 1
        interactions[giver][receiver] += 1
    
    next_month_received = defaultdict(int)
    
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i == j:
                continue
            
            friend_a = friends[i]
            friend_b = friends[j]
            
            if interactions[friend_a][friend_b] > interactions[friend_b][friend_a]:
                next_month_received[friend_a] += 1
            elif interactions[friend_a][friend_b] < interactions[friend_b][friend_a]:
                next_month_received[friend_b] += 1
            else:
                gift_index_a = given[friend_a] - received[friend_a]
                gift_index_b = given[friend_b] - received[friend_b]
                
                if gift_index_a > gift_index_b:
                    next_month_received[friend_a] += 1
                elif gift_index_b >gift_index_a:
                    next_month_received[friend_b] += 1
    return max(next_month_received.values(), default = 0)/2