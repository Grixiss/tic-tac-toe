
from random import randrange


# Tic-tac-toe board
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]


def update_board(move):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == move:
                board[i][j] = "O"
                return
    return board


#updated_board = update_board(4)
#print(updated_board)

def make_list_of_free_fields(move=1):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j == move:
                if board[i][j] == "O" or board[i][j] == "X":
                    return False
                else:
                    return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    move = randrange(8)
    if make_list_of_free_fields(move):
        # update board
        update_board_computer(move)
        # diplay update
        display_board(board, move)

draw_move(board)
