def solution(array, height):
    cnt = 0
    
    for i in range(len(array)):
        if array[i] > height:
            cnt += 1
        else:
            pass
    
    return cnt