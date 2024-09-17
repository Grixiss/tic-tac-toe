"""display_board(board)
    Process:
        For each row in the board:
            Print a row border.
            Print the row with appropriate spacing and borders.
        Print the final row border.

import random

from random import randrange
for i in range(10):
    print(randrange(8))
"""
import random

board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

def display_board(board, move) :
    if move == 1 :
        i = 0
        j = 0
        for row in board :
            print("+-------"  + "+-------" + "+-------" + "+")
            print("|       " + "|"+ "      " + " |"+ "      " + " |")
            print("|   " + str(board[i][2]) + "   |   " + str(board[i][1]) + "   |   " + str(board[i][2]) + "   |")
            print("|       " + "|"+ "      " + " |"+ "      " + " |")
            i += 1
            j += 1
        print("+-------"*3 + "+")
    else :
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
        if  10 > move > 0  :
            display_board(board, move)
        else :
            print("bad")

enter_move(board)

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