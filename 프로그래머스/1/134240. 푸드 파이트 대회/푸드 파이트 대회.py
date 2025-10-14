def solution(food):
    temp = ''
    
    for i in range(1,len(food)):
        temp += str(i)*(food[i]//2)
    
    result = temp + '0' + temp[::-1]
    
    return result