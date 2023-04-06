moves = 0
def clear_board():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def print_board(board):
    for x in board:
        for y in x:
            print(f"_{y}_", end='\t')
        print()


def update_board(board, player, position):
    col = (position - 1) % 3
    row = (position - 1) // 3
    if not check_position(board, row, col):
        print("Invalid Choice, please choose again.")
        return board, player
    board[row][col] = player
    print_board(board)
    global moves 
    moves +=  1
    if check_winner(board,player):
        player = toggle_player(player)
    return board, player


def check_position(board, row, col):
    if row not in range(3) or col not in range(3):
        return False
    if board[row][col] not in range(1, 10):
        return False
    return True


def check_winner(board, player):
    condition1 = (board[0][0] == board[0][1]) and (board[0][1] == board[0][2])
    condition2 = (board[0][0] == board[1][0]) and (board[1][0] == board[2][0])
    condition3 = (board[0][0] == board[1][1]) and (board[1][1] == board[2][2])
    condition4 = (board[1][0] == board[1][1]) and (board[1][1] == board[1][2])
    condition5 = (board[2][0] == board[2][1]) and (board[2][1] == board[2][2])
    condition6 = (board[0][1] == board[1][1]) and (board[1][1] == board[2][1])
    condition7 = (board[0][2] == board[1][2]) and (board[1][2] == board[2][2])
    if condition1 or condition2 or condition3 or condition4 or condition5 or condition6 or condition7:
        return False
    return True


def toggle_player(player):
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    return player


def main():
    board = clear_board()
    print_board(board)
    player = 'X'
    # board, player = update_board(board, player, int(input(f"Player{player}: Choose your move position: ")))
    # print_board(board)
    #moves = 0
    while check_winner(board, player) and moves < 9:
        board, player = update_board(board, player, int(input(f"Player{player}: Choose your move position: ")))
        #moves += 1
    if moves == 9 and check_winner(board, player):
        print("Game drawn..!!")
    if not check_winner(board, player):
        print(f"{player} wins...!!")


main()
