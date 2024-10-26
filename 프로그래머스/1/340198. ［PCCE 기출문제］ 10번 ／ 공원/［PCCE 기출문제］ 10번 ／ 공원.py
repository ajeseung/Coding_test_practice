def solution(mats, park):
    rows = len(park)
    cols = len(park[0])
    
    def can_place(mat_size, r, c):
        if r + mat_size > rows or c + mat_size > cols:
            return False
        for i in range(r, r + mat_size):
            for j in range(c, c + mat_size):
                if park[i][j] != "-1":
                    return False
        return True
    
    mats.sort(reverse = True)
    
    for mat in mats:
        for r in range(rows):
            for c in range(cols):
                if can_place(mat,r,c):
                    return mat
    
    return -1