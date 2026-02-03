def solution(n, tops):
    MOD = 10007
    
    A, B = 1, 0
    
    for t in tops:
        if t == 0:
            nA = (2*A + B) % MOD
            nB = (A+B) % MOD
        else:
            nA = (3*A + 2*B) % MOD
            nB = (A+B) % MOD
        
        A, B = nA, nB
    
    return (A+B) % MOD