from string import ascii_lowercase

def solution(s, skip, index):
    available = [c for c in ascii_lowercase if c not in skip]
    
    result = ''
    
    for char in s:
        i = available.index(char)
        new_char = available[(i + index) % len(available)]
        result += new_char
        
    return result