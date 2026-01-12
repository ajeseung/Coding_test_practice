def solution(my_string, indices):
    indices.sort()
    n = len(my_string)
    cha = ''
    
    print(indices)
    for i in range(n):
        if i not in indices:
            cha += my_string[i]

    return cha