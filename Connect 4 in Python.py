#Michael Householder @Mikeh627 -- Github
#COP 1500
#Connect 4 in Python

import numpy as np      #this array allows for the input of matricies and much more, most importantly matricies for connect 4


ROWS = 6
COLUMNS = 7             #Because these 2 will not change its easier for us to make them all capital, so if we ever want to edit or someone else wants to.

def create_board():
    board = np.zeros((ROWS, COLUMNS))       #This function creates a 6 by 7 matrix.
    return board

def drop_chip(board, row, column, chip):    #This function will let us define our piece(chip) being "dropped"
    board[row][column] = chip

def is_valid(board, column):
    return board[ROWS - 1][column] == 0

def is_not_valid(board, ROWS, COLUMNS):
        print("Move is not valid")

def get_next_open_row(board, column):
    for r in range(ROWS):
        if board[r][column] == 0:
            return r

#Because numpy presents the nums by default top to bottom to resemble the game connect 4 we mirror the matrix which allows for a bottom to top look.
def print_board(board):
    print(np.flip(board, 0))

def final_blow(board, chip):
    #This function checks for the winning moves on the horizontal axis
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == chip and board[r][c + 1] == chip and board[r][c + 2] == chip and board[r][c + 3] == chip:
                return True

    #This function checks for the winning moves on the vertical axis
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == chip and board[r + 1][c] == chip and board[r + 2][c] == chip and board[r + 3][c] == chip:
                return True

    #This function will check for the positive sloped winning moves
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == chip and board[r + 1][c + 1] == chip and board[r + 2][c + 2] == chip and board[r + 3][c + 3] == chip:
                return True

    #This function will check for the negative sloped winning moves
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if board[r][c] == chip and board[r - 1][c + 1] == chip and board[r - 2][c + 2] == chip and board[r - 3][c + 3] == chip:
                return True

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over :
    if turn == 0:
        column = int(input("Player 1 drop your piece (0,6): "))         # this whole if statement goes between player one and player two, until someone connects 4
        
        if is_valid(board, column):
            row = get_next_open_row(board, column)
            drop_chip(board, row, column, 1)

            if is_not_valid(board, ROWS, COLUMNS):
                turn == 0
                print("Move is not valid")
            
            if final_blow(board, 1):
                print("Game over..\nPlayer 1 wins!!!")
                game_over = True

    else:
        column = int(input("Player 2 drop your piece (0,6): "))

        if is_valid(board, column):
            row = get_next_open_row(board, column)
            drop_chip(board, row, column, 2)

            if is_not_valid(board, ROWS, COLUMNS):
                turn != 0
                print("Move is not valid")
        
            if final_blow(board, 2):
                print("Game over..\nPlayer 2 wins!!!")          # this will allow us to display whenever someone connects 4 :D
                game_over = True
                 
    print_board(board)

    turn += 1
    turn = turn % 2             # these 2 "functions" if you will allow us to tell the program whose turn it is.
