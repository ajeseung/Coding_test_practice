def solution(bin1, bin2):
    a = int(bin1, 2)
    b = int(bin2, 2)
    
    result = a + b
    
    answer = ""
    
    while result > 0:
        answer = str(result % 2) + answer
        result //= 2
    
    return answer if answer else "0"
