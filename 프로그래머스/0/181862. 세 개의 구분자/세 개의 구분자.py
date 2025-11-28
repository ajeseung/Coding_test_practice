def solution(myStr):
    for ch in "abc":
        myStr = myStr.replace(ch, " ")
    
    result = myStr.split()
    
    return result if result else ["EMPTY"]