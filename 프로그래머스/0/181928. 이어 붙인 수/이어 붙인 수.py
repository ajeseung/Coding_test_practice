def solution(num_list):
    odds= []
    evens= []
    
    for num in num_list:
        if num % 2 == 0:
            evens.append(str(num))
        else:
            odds.append(str(num))
            
    odds_num = int("".join(odds))
    evens_num = int("".join(evens))
    
    return odds_num + evens_num