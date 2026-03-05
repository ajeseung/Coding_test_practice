from math import gcd

def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = ext_gcd(b,a % b)
    return g, y1, x1 - (a // b) * y1

def crt_one(a1, m1, a2, m2):
    g = gcd(m1, m2)
    diff = a2 - a1
    if diff % g != 0:
        return None
    
    lcm = m1 // g * m2
    
    m1_ = m1 // g
    m2_ = m2 // g
    diff_ = diff // g
    
    gg, x, y = ext_gcd(m1_, m2_)
    inv = x % m2_
    k = (diff_ * inv) % m2_
    
    x0 = (a1 + m1 * k) % lcm
    return x0, lcm

def solution(signals):
    allowed = []
    mods = []
    for G, Y, R in signals:
        P = G + Y + R
        mods.append(P)
        allowed.append(list(range(G, G+Y)))
        
    M = mods[0]
    Rset = set(allowed[0])  # residues mod M

    # Combine iteratively
    for i in range(1, len(signals)):
        P = mods[i]
        A = allowed[i]
        new_set = set()

        for r in Rset:
            for a in A:
                res = crt_one(r, M, a, P)
                if res is None:
                    continue
                x0, L = res
                new_set.add(x0)

        if not new_set:
            return -1

        M = (M // gcd(M, P)) * P  # lcm
        Rset = new_set

    # Minimal x is the minimal residue
    x_min = min(Rset)
    return x_min + 1