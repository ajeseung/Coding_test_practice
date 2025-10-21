def solution(money):
    array = []
    
    array.append(money // 5500)
    array.append(money % 5500)
    
    return array