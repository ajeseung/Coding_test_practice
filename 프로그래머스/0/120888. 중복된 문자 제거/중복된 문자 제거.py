def solution(my_string):
    passed = set()
    result = ""
    
    for ch in my_string:
        if ch not in passed:
            passed.add(ch)
            result += ch
            
    return result