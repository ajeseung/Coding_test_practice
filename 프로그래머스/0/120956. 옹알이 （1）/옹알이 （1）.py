def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    cnt = 0
    
    for babb in babbling:
        over_used = False
        for w in words:
            if babb.count(w) > 1:
                over_used = True
                break
        if over_used:
            continue
        
        tmp = babb
        
        for w in words:
            tmp = tmp.replace(w, " ")
        tmp = tmp.replace(" ", "")    
        
        if tmp == "":
            cnt += 1
    return cnt