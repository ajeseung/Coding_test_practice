def solution(m, n, board):
    total_removed = 0
    
    board = [list(row) for row in board]
    
    while True:
        to_remove = set()
        
        for i in range(m-1):
            for j in range(n-1):
                ch = board[i][j]
                if ch == ' ':
                    continue
                if (ch == board[i][j+1] and ch == board[i+1][j] and ch == board[i+1][j+1]):
                    to_remove.add((i,j))
                    to_remove.add((i+1,j))
                    to_remove.add((i,j+1))
                    to_remove.add((i+1,j+1))
                    
        if not to_remove:
            break
        
        for (i, j) in to_remove:
            board[i][j] = ' '
            
        total_removed += len(to_remove)
        
        
        for j in range(n):
            stack = []
            
            for i in range(m-1, -1, -1):
                if board[i][j] != ' ':
                    stack.append(board[i][j])
            
            idx = m-1
            for ch in stack:
                board[idx][j] = ch
                idx -= 1
            
            for i in range(idx, -1, -1):
                board[i][j] = ' '
                
    return total_removed