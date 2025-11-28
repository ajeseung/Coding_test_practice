def solution(str_list):
    n = len(str_list)
    
    for i in range(n):
        if str_list[i] == "l":
            return str_list[:i]
        elif str_list[i] == "r":
            return str_list[i+1:]
        
    return []