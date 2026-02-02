# import math

def solution(n, w, num):
    r = (num - 1) // w          # num의 층(0-index)
    pos = (num - 1) % w         # 그 층에서의 진행 인덱스(0..w-1)
    
    # num이 있는 실제 열(column) 구하기
    if r % 2 == 0:              # L -> R
        c = pos
    else:                        # R -> L
        c = w - 1 - pos

    full_rows = n // w
    rem = n % w

    # num이 있는 열의 전체 높이(height) 계산
    height = full_rows
    if rem != 0:
        last_r = full_rows      # 마지막(부분) 층의 index
        if last_r % 2 == 0:     # 마지막 층이 L -> R
            if c < rem:
                height += 1
        else:                   # 마지막 층이 R -> L
            if c >= w - rem:
                height += 1

    return height - r
