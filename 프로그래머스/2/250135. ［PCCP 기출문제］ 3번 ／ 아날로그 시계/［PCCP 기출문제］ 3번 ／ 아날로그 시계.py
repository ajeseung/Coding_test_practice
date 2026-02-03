def solution(h1, m1, s1, h2, m2, s2):
    t1 = h1*3600 + m1*60 + s1
    t2 = h2*3600 + m2*60 + s2
    
    def f(T):
        if T <= 0:
            return 0
        
        cnt_sm = (T*59 - 1) //3600 + 1
        cnt_sh = (T*719 - 1) // 43200 + 1
        
        dup = 1
        
        if T > 43200:
            dup += 1
        
        return cnt_sm + cnt_sh - dup
    
    def g(T):
        if T < 0:
            return 0
        
        cnt_sm = (T * 59) // 3600 + 1
        cnt_sh = (T * 719) // 43200 + 1
        
        dup = 1
        if T >= 43200:
            dup += 1
            
        return cnt_sm + cnt_sh - dup
    
    return g(t2) - f(t1)