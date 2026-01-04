def solution(myString):
    parts = myString.split('x')
    result = []
    
    for s in parts:
        result.append(len(s))
        
    return result