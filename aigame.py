import os

def print_board(board):
    print("{}|{}|{}".format(board[0],board[1],board[2]))
    print("-----")
    print("{}|{}|{}".format(board[3],board[4],board[5]))
    print("-----")
    print("{}|{}|{}".format(board[6],board[7],board[8]))

def toggle_mark(mark):
    if mark == "X":
        return "O"
    return "X"

def check_winner(board):
    if board[0]==board[1] and board[1]==board[2] and board[0] != ' ':
        return 1
    elif board[3]==board[4] and board[4]==board[5] and board[3] != ' ':
        return 1
    elif board[6]==board[7] and board[7]==board[8] and board[6] != ' ':
        return 1
    elif board[0]==board[3] and board[3]==board[6] and board[0] != ' ':
        return 1
    elif board[1]==board[4] and board[4]==board[7] and board[1] != ' ':
        return 1
    elif board[2]==board[5] and board[5]==board[8] and board[2] != ' ':
        return 1
    elif board[0]==board[4] and board[4]==board[8] and board[0] != ' ':
        return 1
    elif board[2]==board[4] and board[4]==board[6] and board[2] != ' ':
        return 1
    elif board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ':
        return 2
    else:
        return 0
def play_game(board,place,mark):
    while place not in range(1,10):
        place = int(input("Invalid input. Please input a valid cell number to mark: "))
    if(board[place-1]== ' '):
        board[place-1] = mark
    else:
        print("The selected cell is not empty. Please select an empty cell from 1-9:")
        place = int(input())
        play_game(board,place, mark)
    return board[:]

def choices(board):
    choice = []
    for i,x in enumerate(board):
        if x == ' ':
            choice.append(i+1)
    return choice
            
def best_move(board,mark):
    depth = 0
    choice_list = choices(board)
    win_list = {}
    draw_list = {}
    for x in choice_list:
        score,deep = minimax(board[:], mark, x, True, depth)
        if score == 1:
            win_list[deep] = x
        elif score == 0:
            draw_list[deep] = x   
    if win_list:
        min_depth = min(list(win_list.keys()))
        return win_list[min_depth]
    min_depth = min(list(draw_list.keys()))
    return draw_list[min_depth]
        
def minimax(board, mark, choice, ismax,depth):
    temp_board = play_game(board[:], choice, mark)
    if check_winner(temp_board) == 1:
        if ismax:
            return 1,depth
        return -1,depth
    elif check_winner(temp_board) == 2:
        return 0,depth
    if ismax:
        best_score = -float('inf')
        mark = toggle_mark(mark)
        choice_list = choices(temp_board)
        deep = depth
        for choice in choice_list:
            temp,depth = minimax(temp_board[:], mark, choice, False, depth+1)
            best_score = max(best_score, temp)
            if temp == best_score:
                deep = depth
        return best_score,deep
    else:
        best_score = float('inf')
        mark = toggle_mark(mark)
        choice_list = choices(temp_board)
        deep = depth
        for choice in choice_list:
            temp, depth = minimax(temp_board[:], mark, choice, True, depth+1)
            best_score = min(best_score, temp)
            if best_score == temp:
                deep = depth
        return best_score,deep
 
        
def main():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game = 0
    os.system('clear')
    print("TicTacToe Game by Sai Ravula")    
    mark = input("Choose your symbol as 'X' or 'O': ")
    while mark not in ['X','O','x','o']:
        mark = input("Improper input choose either 'X' or 'O': ")
    mark = mark.capitalize()
    player = mark    
    while not game:
        os.system('clear')
        print("TicTacToe Game by Sai Ravula")
        print("Human Player >>> {} | Computer >>> {}".format(player,toggle_mark(player)))
        print_board(board)
        print("Player-{}'s chance. Choose an empty cell from 1-9 to mark:".format(player))
        place = int(input())
        board = play_game(board,place,mark)
        game = check_winner(board)
        if game: break
        mark = toggle_mark(mark)
        board = play_game(board, best_move(board,mark), mark)
        game = check_winner(board)
        if game: break
        mark = toggle_mark(mark)
    os.system('clear')
    print("TicTacToe Game by Sai Ravula")
    print("Human >>> {} | Computer >>> {}".format(player,toggle_mark(player)))
    print_board(board)
        
    if(game == 2):
        print("Game Tied")
    else:
        print("Player-{} has won.".format(mark))

main()