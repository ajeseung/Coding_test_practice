def solution(board, k):
    answer = 0
    n = len(board)
    m = len(board[0])
    
    for i in range(n):
        max_j = min(k-i, m-1)
        if max_j < 0:
            break
            
        for j in range(max_j+1):
            answer += board[i][j]
    return answer