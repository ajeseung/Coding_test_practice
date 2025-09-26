def solution(dots):
    def parallel(p1, p2, p3, p4):
        x1, y1 = p1; x2, y2 = p2
        x3, y3 = p3; x4, y4 = p4
        return (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1)

    a, b, c, d = dots
    return 1 if (parallel(a, b, c, d) or
                 parallel(a, c, b, d) or
                 parallel(a, d, b, c)) else 0
