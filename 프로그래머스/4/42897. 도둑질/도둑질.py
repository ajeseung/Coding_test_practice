def rob(arr):
    prev2 = 0
    prev1 = 0
    for i in arr:
        cur = max(prev1, prev2 + i)
        prev1, prev2 = cur, prev1
    
    return prev1

def solution(money):
    n = len(money)
    
    if n == 3:
        return max(money)
    
    case_a = rob(money[:-1])
    case_b = rob(money[1:])
    
    return max(case_a,case_b)