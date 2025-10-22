def solution(num_list):
    for i in range(len(num_list)):
        print(num_list[i])
        if num_list[i] < 0:
            return i
        else:
            pass
    
    return -1