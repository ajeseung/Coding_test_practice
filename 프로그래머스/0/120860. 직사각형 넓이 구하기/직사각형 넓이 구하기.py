def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    
    len_x = max(x) - min(x)
    len_y = max(y) - min(y)
    
    return len_x * len_y