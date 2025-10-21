def solution(n, numlist):
    array = []
    
    for i in range(len(numlist)):
        if numlist[i] % n == 0:
            array.append(numlist[i])
        else:
            pass
        
    return array