def solution(score):
    avg = [(e+m) / 2 for e,m in score]
    
    result = []
    
    for a in avg:
        rank = 1
        for b in avg:
            if b > a:
                rank += 1
        result.append(rank)
        
    return result