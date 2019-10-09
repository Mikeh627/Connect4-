
#Michael Householder @Mikeh627 -- Github
#COP 1500
#Connect 4 in Python

import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece():
    pass

def is_valid():
    pass



board = create_board()
end = False
turn = 0

while not end:
    if turn == 0:
        column = int(input("Player 1 drop your piece (0,7): "))

    else:
        column = int(input("Player 2 drop your piece (0,7): "))

    turn += 1
    turn = turn % 2
