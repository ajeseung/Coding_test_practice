def solution(price, money, count):
    total = 0
    for i in range(count+1):
        total += price * i
        print(total)
    
    if total > money:
        return total - money
    else:
        return 0