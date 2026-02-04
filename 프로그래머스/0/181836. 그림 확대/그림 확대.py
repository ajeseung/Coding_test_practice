def solution(picture, k):
    answer = []
    
    for row in picture:
        widend = ''.join(ch*k for ch in row)
    
        for _ in range(k):
            answer.append(widend)
        
    return answer