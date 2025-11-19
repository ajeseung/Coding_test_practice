def solution(routes):
    routes.sort(key = lambda x:x[1])
    
    count = 0
    camera_pos = -30001
    
    for start,end in routes:
        if start > camera_pos:
            count += 1
            camera_pos = end
            
    return count