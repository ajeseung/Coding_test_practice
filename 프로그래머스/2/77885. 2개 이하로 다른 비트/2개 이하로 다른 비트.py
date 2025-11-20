def solution(numbers):
    ans = []
    
    for x in numbers:
        if x % 2 == 0:
            ans.append(x+1)
        else:
            b = bin(x)[2:]
            x_ = b.rfind('0')
            if x_ == -1:
                b = '10' + b[1:]
            else:
                b = b[:x_] + '10' + b[x_+2:]
        
            ans.append(int(b,2))
    
    return ans
        