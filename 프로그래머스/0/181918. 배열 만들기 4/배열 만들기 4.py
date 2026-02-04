def solution(arr):
    stk = []
    i = 0
    n = len(arr)
    
    while i < n:
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif len(stk) != 0 and stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif len(stk) != 0 and stk[-1] >= arr[i]:
            del stk[-1]
    
    
    return stk