def solution(n, arr1, arr2):
    answer = []
    
    for a, b in zip(arr1, arr2):
        row = a|b
        bits = f"{row:0{n}b}"
        line = bits.replace('1', '#').replace('0',' ')
        answer.append(line)
    
    return answer