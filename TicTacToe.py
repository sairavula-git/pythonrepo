import os
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = 1

game = 0  # 3 Conditions 0-> Running 1-> Player Win 2-> Tie
mark = 'X'

def print_board():
    print("{}|{}|{}".format(board[0],board[1],board[2]))
    print("-----")
    print("{}|{}|{}".format(board[3],board[4],board[5]))
    print("-----")
    print("{}|{}|{}".format(board[6],board[7],board[8]))

def check_winner():
    if board[0]==board[1] and board[1]==board[2] and board[0]!=' ':
        return 1
    elif board[3]==board[4] and board[4]==board[5] and board[3]!=' ':
        return 1
    elif board[6]==board[7] and board[7]==board[8] and board[6]!=' ':
        return 1
    elif board[0]==board[3] and board[3]==board[6] and board[0]!=' ':
        return 1
    elif board[1]==board[4] and board[4]==board[7] and board[1]!=' ':
        return 1
    elif board[2]==board[5] and board[5]==board[8] and board[2]!=' ':
        return 1
    elif board[0]==board[4] and board[4]==board[8] and board[0]!=' ':
        return 1
    elif board[2]==board[4] and board[4]==board[6] and board[2]!=' ':
        return 1
    elif board[0] != ' ' and board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ':
        return 2
    else:
        return 0

def play_game(place,mark):
    if(board[place-1]== ' '):
        board[place-1] = mark
    else:
        print("The selected cell is not empty. Please select an empty cell from 1-9:")
        place = int(input())
        play_game(place, mark)

while not game:
    os.system('cls')
    print("TicTacToe Game by Sai Ravula")
    print("Player-1 >>> 'X' | Player-2 >>> 'O'")
    print_board()
    print("Player-{}'s chance. Choose an empty cell from 1-9 to mark:".format(player))
    place = int(input())
    play_game(place,mark)
    game = check_winner()
    if game: break
    if player%2 == 0:
        player = 1
        mark = 'X'
    else:
        player = 2
        mark = 'O'
os.system('cls')
print("TicTacToe Game by Sai Ravula")
print("Player-1 >>> 'X' | Player-2 >>> 'O'")
print_board()
    
if(game == 2):
    print("Game Tied")
else:
    print("Player-{} has won.".format(player))