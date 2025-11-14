def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        filtered = ''.join([ch for ch in tree if ch in skill])
        
        if skill.startswith(filtered):
            answer += 1
    return answer