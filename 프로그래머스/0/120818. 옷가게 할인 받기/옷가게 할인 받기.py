def solution(price):
    pay = 0
    if 10 <= price < 100000:
        pay = price
    elif 100000 <= price < 300000:
        pay = price * 0.95
    elif 300000 <= price < 500000:
        pay = price * 0.9
    elif 500000 <= price:
        pay = price * 0.8
    
    return int(pay)