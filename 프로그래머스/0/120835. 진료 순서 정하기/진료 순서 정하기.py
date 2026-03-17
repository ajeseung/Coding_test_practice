def solution(emergency):
    sorted_list = sorted(emergency, reverse = True)
    # print(sorted_list)
    
    return [sorted_list.index(x) + 1 for x in emergency]