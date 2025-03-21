from itertools import product

def solution(users, emoticons):
    answer = [0,0]
    
    discounts = [10,20,30,40]
    n = len(emoticons)
    
    for rates in product(discounts, repeat=n):
        plus_users = 0
        total_sales = 0
        
        
        for user_discount, user_threshold in users:
            user_total= 0
            
            for i in range(n):
                if rates[i] >= user_discount:
                    discounted_price = emoticons[i] *(100-rates[i]) // 100
                    user_total += discounted_price
                    
            if user_total >= user_threshold:
                plus_users += 1
            
            else:
                total_sales += user_total
                
        if plus_users > answer[0] or (plus_users == answer[0] and total_sales > answer[1]):
            answer = [plus_users, total_sales]
    
    return answer