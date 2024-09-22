
#cisco range function final project
"""
from random import randrange

for i in range(10):
    print(randrange(8))
"""
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]


#gestion update du board avec le move user
def update_board(move):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == move:
                board[i][j] = "O"
                return
    return board

#gestion des moves disponibles
def list_of_free_fields(move):
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
            if list_of_free_fields(move):
                #update board
                update_board(move)
                #diplay update
                display_board(board, move)
                #break #exit if the move is OK
            else :
                print("Position has already taken. Choose another.")
                #move = int(input("enter a number between 1 to 9 :"))
        else :
            print("Invalid input. Please, enter a number between 1 and 9.")

enter_move(board)


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

def draw_move(board):
    # The function draws the computer's move and updates the board.


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

3. make_list_of_free_fields(board)

    Input: Current board state.
    Output: List of free cells in the format (row, column).
    Process:
        Initialize an empty list for free fields.
        For each cell in the board:
            If the cell is not occupied by 'O' or 'X':
                Add the cell's (row, column) to the free fields list.
        Return the list of free fields.

4. victory_for(board, sign)"""




