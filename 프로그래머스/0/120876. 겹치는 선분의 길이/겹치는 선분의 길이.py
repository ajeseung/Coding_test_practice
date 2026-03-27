def solution(lines):
    count = [0] * 201
    answer = 0
    
    for start, end in lines:
        for i in range(start, end):
            count[i+100] += 1
    
    for x in count:
        if x >= 2:
            answer += 1
    
    return answer