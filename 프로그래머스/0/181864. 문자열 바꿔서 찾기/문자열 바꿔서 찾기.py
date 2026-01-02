def solution(myString, pat):
    n = len(myString)
    newmyString = ""
    
    for i in range(n):
        if myString[i] == "A":
            newmyString += "B"
        else:
            newmyString += "A"
            
    if pat in newmyString:
        return 1
    else:
        return 0