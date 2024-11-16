# Libraries
import numpy as np
import pygame

# Variables
ROWS = 3
COLS = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

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

def draw_lines():
    pygame.draw.line(window, BLACK, (200,0), (200,600), 10)
    pygame.draw.line(window, BLACK, (400,0), (400,600), 10)
    pygame.draw.line(window, BLACK, (0,200), (600,200), 10)
    pygame.draw.line(window, BLACK, (0,400), (600,400), 10)

def is_winning_move(player):
    if player == 1:
        announcement = "Player 1 Won"
    else:
        announcement = "Player 2 Won"
    
    for row in range(ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            print(announcement)
            return True
    for col in range(COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            print(announcement)
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print(announcement)
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print(announcement)
        return True

# Initiate board
board = np.zeros((ROWS,COLS))

game_over = False

Turn = 0

pygame.init()
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tic-Tac-Toe")
window.fill(WHITE)
draw_lines()
pygame.display.update()
pygame.time.wait(2000)

# while not game_over:
#     if Turn % 2 == 0:
#         # Player 1
#         row = int(input("Player 1: Choose row number (0-2): "))
#         col = int(input("Player 1: Choose column number (0-2): "))
#         if is_valid_mark(row, col):
#             mark(row, col, 1)
#             if is_winning_move(1):
#                 game_over = True
#         else:
#             Turn -= 1
#     else:
#         # Player 2
#         row = int(input("Player 2: Choose row number (0-2): "))
#         col = int(input("Player 2: Choose column number (0-2): "))
#         if is_valid_mark(row, col):
#             mark(row, col, 2)
#             if is_winning_move(2):
#                 game_over = True
#         else:
#             Turn -= 1

#     Turn += 1
#     print(board)
#     if game_over == True:
#         print("Game Over")