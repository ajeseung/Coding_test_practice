def solution(n):
    digits = "124"
    answer = ""
    
    while n>0:
        n -= 1
        answer = digits[n%3] + answer
        n //= 3
        
    return answer