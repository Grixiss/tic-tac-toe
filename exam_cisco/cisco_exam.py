from random import randrange

#cisco range function final project
"""
for i in range(10):
    print(randrange(8))
"""
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]


#gestion update du board avec le move user
def update_board_user(move):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == move:
                board[i][j] = "O"
                return
    return board

def update_board_computer(move):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == move:
                board[i][j] = "X"
                return
    return board

#gestion des moves disponibles
def make_list_of_free_fields(move):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == move:  # Vérifier si la case contient encore le move (non "O" ou "X")
                return True
    return False

def display_board(board, move) :
        i = 0
        j = 0
        for row in board :
            print("+-------"  + "+-------" + "+-------" + "+")
            print("|       " + "|"+ "      " + " |"+ "      " + " |")
            print("|   " + str(board[i][0]) + "   |   " + str(board[i][1]) + "   |   " + str(board[i][2]) + "   |")
            print("|       " + "|"+ "      " + " |"+ "      " + " |")
            i += 1
            j += 1
        print("+-------"*3 + "+")



#display_board(board)

def enter_move(board):
    while True:
        move = int(input("enter a number between 1 to 9 :"))
        if  10 > move > 0 :
            #check is move in authorized
            #list_of_free_fields(move,board)
            if make_list_of_free_fields(move):
                #update board
                update_board_user(move)
                #diplay update
                display_board(board, move)
            else :
                print("Position has already taken. Choose another.")
                #move = int(input("enter a number between 1 to 9 :"))
        else :
            print("Invalid input. Please, enter a number between 1 and 9.")



def victory_for(board, sign):
    # Horizontal check
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True

    # Vertical check
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True

    # diagonal from top left top bottom right
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True

    # diagonal from top right to bottom left
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    #last possibility, no winner
    return False



def draw_move(board):
        move = randrange(8)
        if make_list_of_free_fields(move):
            # update board
            update_board_computer(move)
            # diplay update
            display_board(board, move)


def play_game(board):
    while True:
        display_board(board, None)
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board, None)
            print("Congratulations! You win!")
            break
        if not make_list_of_free_fields(0):
            display_board(board, None)
            print("It's a tie!")
            break
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board, None)
            print("The computer wins!")
            break
        if not make_list_of_free_fields(0):
            display_board(board, None)
            print("It's a tie!")
            break

play_game(board)

"""
2. enter_move(board)

    Input: Current board state.
    Output: Update the board with the user's move.
    Process:
        Repeat until a valid move is entered:
            Prompt the user for a move (number 1-9).
            Validate if the input is an integer between 1 and 9.
            Calculate the row and column based on the user's input.
            Check if the selected cell is empty:
                If yes, place 'O' in the cell and break the loop.
                If no, prompt the user to choose another cell.

4. victory_for(board, sign)"""




