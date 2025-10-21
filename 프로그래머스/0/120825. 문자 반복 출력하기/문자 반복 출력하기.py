def solution(my_string, n):
    str1 = ''
    
    for i in range(len(my_string)):
        str1 += my_string[i]*n
        
    return str1