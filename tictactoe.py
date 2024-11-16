# Libraries
import numpy as np

# Variables
ROWS = 3
COLS = 3

# Functions
def mark(row, col, player):
    board[row][col] = player

def is_valid_mark(row, col):
    return board[row][col] == 0

def is_board_full():
    for col in range(COLS):
        for row in range(ROWS):
            if board[row][col] == 0:
                return False
    return True

board = np.zeros((ROWS,COLS))

print(board)
mark(1,0,2)
print(board)
print(is_valid_mark(1,0))