def solution(rank, attendance):
    students = []
    
    for i, (r,can) in enumerate(zip(rank, attendance)):
        if can:
            students.append((r,i))
            
    students.sort()
    
    a = students[0][1]
    b = students[1][1]
    c = students[2][1]
    
    return 10000*a + 100 * b + c