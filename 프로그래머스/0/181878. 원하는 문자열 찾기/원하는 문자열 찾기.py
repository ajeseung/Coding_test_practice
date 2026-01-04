def solution(myString, pat):
    new_myString = myString.lower()
    new_pat = pat.lower()
    
    if new_pat in new_myString:
        return 1
    else:
        return 0
    