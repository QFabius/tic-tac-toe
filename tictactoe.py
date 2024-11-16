# Libraries
import numpy as np
import pygame
import math

# Parameters
ROWS = 3
COLS = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

CIRCLE = pygame.image.load('img/circle.png')
CROSS = pygame.image.load('img/cross.png')

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

def draw_board():
    for col in range(COLS):
        for row in range(ROWS):
            if board[row][col] == 1:
                window.blit(CIRCLE, ((col*200)+50, (row*200)+50))
            elif board[row][col] == 2:
                window.blit(CROSS, ((col*200)+50, (row*200)+50))
    pygame.display.update()
            

def draw_lines():
    pygame.draw.line(window, BLACK, (200,0), (200,600), 10)
    pygame.draw.line(window, BLACK, (400,0), (400,600), 10)
    pygame.draw.line(window, BLACK, (0,200), (600,200), 10)
    pygame.draw.line(window, BLACK, (0,400), (600,400), 10)

def is_winning_move(player):
    if player == 1:
        winning_color = BLUE
    else:
        winning_color = RED
    
    for row in range(ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            pygame.draw.line(window, winning_color, (10, (row*200)+100), (WIDTH-10, (row*200)+100), 10)
            return True
    for col in range(COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            pygame.draw.line(window, winning_color, ((col*200)+100, 10), ((col*200)+100, HEIGHT-10), 10)
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        pygame.draw.line(window, winning_color, (10, 10), (590, 590), 10)
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        pygame.draw.line(window, winning_color, (590, 590), (10, 10), 10)
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

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

            if Turn % 2 == 0:
                # Player 1
                row = math.floor(event.pos[1]/200)
                col = math.floor(event.pos[0]/200)
                if is_valid_mark(row, col):
                    mark(row, col, 1)
                    if is_winning_move(1):
                        game_over = True
                else:
                    Turn -= 1
            else:
                # Player 2
                row = math.floor(event.pos[1]/200)
                col = math.floor(event.pos[0]/200)
                if is_valid_mark(row, col):
                    mark(row, col, 2)
                    if is_winning_move(2):
                        game_over = True
                else:
                    Turn -= 1

            Turn += 1
            print(board)
            draw_board()
    if is_board_full():
        game_over = True
    if game_over == True:
        print("Game Over")
        pygame.time.wait(2000)
        board.fill(0)
        window.fill(WHITE)
        draw_lines()
        draw_board()
        game_over = False
        pygame.display.update()