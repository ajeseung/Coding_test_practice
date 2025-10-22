def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for v in vowels:
        my_string = my_string.replace(v, '')
    return my_string
