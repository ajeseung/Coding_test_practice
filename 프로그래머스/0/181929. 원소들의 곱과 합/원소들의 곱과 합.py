def solution(num_list):
    list_sum = 0
    multi = 1
    for i in range(len(num_list)):
        list_sum += num_list[i]
        multi *= num_list[i]

    if list_sum**2 < multi:
        return 0
    else:
        return 1