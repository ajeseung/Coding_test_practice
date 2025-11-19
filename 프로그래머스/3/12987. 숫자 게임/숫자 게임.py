def solution(A, B):
    A.sort()
    B.sort()
    
    i = 0
    j = 0
    score = 0
    N = len(A)
    
    while i < N and j < N:
        if B[j] > A[i]:
            score += 1
            i += 1
            j += 1
        else:
            j += 1
            
    return score