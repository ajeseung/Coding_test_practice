def solution(n, m, x, y, r, c, k):
    #가능 여부 판별
    need = abs(x-r) + abs(y-c)
    if need > k or (k-need) % 2 !=0:
        return "impossible"
    
    moves = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
    
    cx, cy = x,y
    remain = k
    path = []
    
    while remain > 0:
        for ch, dx, dy in moves:
            nx, ny = cx+dx, cy+dy
            
            if 1 <= nx <= n and 1 <= ny <= m:
                rem = remain - 1
                dist = abs(nx - r) + abs(ny - c)
                
                if dist <= rem and (rem -dist) % 2 == 0:
                    path.append(ch)
                    cx, cy = nx, ny
                    remain = rem
                    break
        # else:
        #     return "impossible"
    return "".join(path)
                    