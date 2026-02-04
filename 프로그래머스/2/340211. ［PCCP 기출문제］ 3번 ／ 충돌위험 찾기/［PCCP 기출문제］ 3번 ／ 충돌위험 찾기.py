from collections import defaultdict

def solution(points, routes):
    P = [None] + points
    
    def build_path(route):
        r,c = P[route[0]]
        path = [(r,c)]
        
        for idx in range(1, len(route)):
            tr, tc = P[route[idx]]
            
            while r != tr or c != tc:
                if r != tr:
                    r += 1 if tr > r else -1
                else:
                    c += 1 if tc > c else -1
                path.append((r,c))
        
        return path
    
    robot_paths = [build_path(route) for route in routes]
    maxT = max(len(p) for p in robot_paths)
    
    i = 0
    for t in range(maxT):
        pos_count = defaultdict(int)
        for path in robot_paths:
            if t < len(path):
                pos_count[path[t]] += 1
            
        for cnt in pos_count.values():
            if cnt >= 2:
                i += 1
        
    return i