def solution(board):
    # O와 X의 개수를 셉니다.
    o_count = sum(row.count('O') for row in board)
    x_count = sum(row.count('X') for row in board)

    # 가로, 세로, 대각선에서 승리 조건을 확인하는 함수
    def check_winner(player):
        # 가로 확인
        for row in board:
            if row == player * 3:
                return True
        # 세로 확인
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == player:
                return True
        # 대각선 확인
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False

    o_win = check_winner('O')
    x_win = check_winner('X')

    # 1. X의 개수가 O보다 많으면 안됨.
    if x_count > o_count:
        return 0
    # 2. O의 개수가 X보다 1개보다 많이 많으면 안됨.
    if o_count > x_count + 1:
        return 0
    # 3. O가 승리했는데 O와 X의 개수가 같으면 안됨.
    if o_win and o_count != x_count + 1:
        return 0
    # 4. X가 승리했는데 O와 X의 개수가 다르면 안됨.
    if x_win and o_count != x_count:
        return 0
    # 5. O와 X가 동시에 승리하면 안됨.
    if o_win and x_win:
        return 0

    return 1
