def solution(num_list, n):
    array = []
    i = 0
    
    while n * i < len(num_list):
        array.append(num_list[0+n*i])
        i += 1
    
    return array