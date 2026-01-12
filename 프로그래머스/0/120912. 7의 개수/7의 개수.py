def solution(array):
    cha = ''
    answer = 0
    
    for i in range(len(array)):
        cha += str(array[i])
    
    print(cha)
    
    for j in range(len(cha)):
        if cha[j] == '7':
            answer += 1
            
    return answer