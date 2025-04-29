def solution(n):
    list_a = []
    
    list_a.append(0)
    list_a.append(1)

    
    for i in range(2,n+1):
        temp = list_a[i-1] + list_a[i-2]
        list_a.append(temp)
        
    return list_a[n] % 1234567
        



