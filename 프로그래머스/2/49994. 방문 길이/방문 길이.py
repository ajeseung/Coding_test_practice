def solution(dirs):
    moves = {'U': (0,1),'D': (0,-1),'R': (1,0),'L': (-1,0)}
    
    x = y = 0
    
    passed_points = set()
    
    for ch in dirs:
        dx, dy = moves[ch]
        nx, ny = x + dx, y + dy
        
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue
            
        e = ((x,y), (nx,ny))
        if e[1] < e[0]:
            e = (e[1], e[0])
            
        passed_points.add(e)
        x,y = nx, ny
        
    return len(passed_points)