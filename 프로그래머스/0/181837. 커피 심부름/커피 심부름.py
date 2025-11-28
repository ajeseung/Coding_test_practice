def solution(order):
    n = len(order)
    result = 0
    
    for drink in order:
        if drink in ("iceamericano", "americanoice", "hotamericano", "americanohot", "americano", "anything"):
            result += 4500
        elif drink in ("icecafelatte", "cafelatteice", "cafelatte", "hotcafelatte", "cafelattehot"):
            result += 5000
    
    return result