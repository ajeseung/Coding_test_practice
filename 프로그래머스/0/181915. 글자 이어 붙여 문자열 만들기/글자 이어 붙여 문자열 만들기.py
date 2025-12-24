def solution(my_string, index_list):
    n = len(index_list)
    answer = ''
    
    for i in range(n):
        answer += my_string[index_list[i]]
        
    return answer