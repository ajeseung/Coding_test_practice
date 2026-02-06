def solution(i, j, k):
    answer = 0
    char = ""
    
    for n in range(i,j+1):
        char += str(n)
    
    return char.count(str(k))