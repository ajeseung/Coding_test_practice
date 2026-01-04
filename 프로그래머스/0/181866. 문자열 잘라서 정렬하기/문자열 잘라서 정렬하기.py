def solution(myString):
    parts = myString.split('x')
    answer = []
    
    for s in parts:
        if s != '':
            answer.append(s)
    answer.sort()
    return answer