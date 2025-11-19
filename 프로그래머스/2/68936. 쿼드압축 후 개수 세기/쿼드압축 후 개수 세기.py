def solution(arr):
    n = len(arr)
    zero = 0
    one = 0

    def compress(x, y, size):
        nonlocal zero, one

        # 1. 이 영역이 모두 같은 값인지 확인
        first = arr[x][y]
        same = True
        for i in range(x, x + size):
            if not same:
                break
            
            for j in range(y, y + size):
                if arr[i][j] != first:
                    same = False
                    break
            
        
        if same:
            if first == 0:
                zero += 1
            else:
                one += 1
            return
        
        half = size //2
        compress(x,y,half)
        compress(x, y+half, half)
        compress(x+half, y, half)
        compress(x+half, y+half, half)
        
    
    compress(0,0,n)
    return [zero,one]