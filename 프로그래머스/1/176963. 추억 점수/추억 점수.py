def solution(name, yearning, photo):
    yearning_dict = {name[i]: yearning[i] for i in range(len(name))}
    
    result = []
    
    for people in photo:
        score = sum(yearning_dict.get(person,0) for person in people)
        result.append(score)
    
    return result