def solution(spell, dic):
    target = sorted(spell)
    
    for word in dic:
        if sorted(word) == target:
            return 1
    
    return 2