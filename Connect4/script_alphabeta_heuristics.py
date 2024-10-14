#! /usr/bin/env python3 
# -*- coding: utf-8 -*-

import numpy as np

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True

    # Check columns
    for col in range(7):
        for row in range(3):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True

    # Check diagonals (positive slope)
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True

    # Check diagonals (negative slope)
    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == player and board[row+1][col-1] == player and board[row+2][col-2] == player and board[row+3][col-3] == player:
                return True

    return False



def check_center(board, player) : 
    ### Check if the central positions are occupied by the player
    count = 0 
    for row in range(6):
        for col in range(2,5) :
            if board[row][col] == player:
                count += 1
    return count



def check_corners(board, player) : 
    ### Check if the corner positions are occupied by the player
    count = 0 
    for row in range(6):
        for col in range(7) :
            if board[row][col] == player and (row == 0 or row == 5) and (col == 0 or col == 6):
                count += 1
    return count



def check_3positions(board, player) : 
    ### Check if the player has 3 positions in a row
    count = 0 
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player:
                count += 5

    for col in range(7):
        for row in range(3):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player:
                count += 5
    
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player:
                count += 1
    
    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == player and board[row+1][col-1] == player and board[row+2][col-2] == player:
                count += 5
    return count

def check_holes(board, player) :
    ### Check if the player miss one position in the middle of 4 positions
    count = 0
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+3] == player and board[row][col+2] == ' ':
                count += 3
    
    for col in range(7):
        for row in range(3):
            if board[row][col] == player and board[row+1][col] == player and board[row+3][col] == player and board[row+2][col] == ' ':
                count += 3

    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+3][col+3] == player and board[row+2][col+2] == ' ':
                count += 3
    
    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == player and board[row+1][col-1] == player and board[row+3][col-3] == player and board[row+2][col-2] == ' ':
                count += 3
    
    return count



# Function to evaluate the score of a board state
def evaluate(board):
    score = 0
    if check_win(board, 'X'):
        score = 100
    elif check_win(board, 'O'):
        score = -100
    
    score += check_center(board, 'X') - check_center(board, 'O')
    score += check_corners(board, 'X') - check_corners(board, 'O')
    score += check_3positions(board, 'X') - check_3positions(board, 'O')
    score += check_holes(board, 'X') - check_holes(board, 'O')
    return score
    

# Function to print the board
def print_board(board):
    print()
    print()
    for row in range(6):
        print(f"|   |   |   |   |   |   |   |")
        print(f"| {board[row][0]} | {board[row][1]} | {board[row][2]} | {board[row][3]} | {board[row][4]} | {board[row][5]} | {board[row][6]} |")
        print(f"____________________________")
    print()
    print()

# Function to generate all possible moves
def generate_moves(board):
    moves = []
    for col in range(7):
        if board[0][col] == ' ':  #If upper cell of every col is empty, select that col 
            moves.append(col)
    return moves

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or check_win(board, 'X') or check_win(board, 'O'):  #Check if we are in a leaf node 
        return evaluate(board)

    if maximizing_player:   #If computer is playing 
        max_eval = float('-inf')  #Set maximizer to lowest possible value 
        for move in generate_moves(board):
            new_board = board.copy()
            for row in range(5, -1, -1):  #From lower to upper row 
                if new_board[row][move] == ' ':
                    new_board[row][move] = 'X'
                    break                  #If there is a new position stop generating and call minimax at lower level 
            eval = minimax(new_board, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:             #Alpha-Beta pruning 
                break                     # Beta pruning 
        return max_eval
    
    else:      #If human/minimizer is playing 
        min_eval = float('inf') #human is minimizer so you set the minimizer value as high as possible 
        for move in generate_moves(board):
            new_board = board.copy()
            for row in range(5, -1, -1):
                if new_board[row][move] == ' ':
                    new_board[row][move] = 'O'
                    break
            eval = minimax(new_board, depth-1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break               #Alpha pruning 
        return min_eval


# Function to make the computer's move
def make_computer_move(board):
    best_score = float('-inf')
    best_move = None
    for move in generate_moves(board):
        new_board = board.copy()
        for row in range(5, -1, -1):
            if new_board[row][move] == ' ':
                new_board[row][move] = 'X'
                break
        score = minimax(new_board, 5, float('-inf'), float('inf'), False)    #Init alpha=-inf, beta=+inf
        if score > best_score:
            best_score = score
            best_move = move
    for row in range(5, -1, -1):
        if board[row][best_move] == ' ':
            board[row][best_move] = 'X'
            break

# Main game loop
def play_game():
    board = np.full((6, 7), ' ')
    print_board(board)
    while True:
        # Player's move
        while True:
            try:
                col = int(input("Enter your move (0-6): "))
                if col < 0 or col > 6 or board[0][col] != ' ':
                    raise ValueError
                break
            except ValueError:
                print("Invalid move. Try again.")
        for row in range(5, -1, -1):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                break       #End of player's turn 
        print_board(board)
        if check_win(board, 'O'):
            print("You win!")
            break
        if ' ' not in board:
            print("It's a draw!")
            break

        # Computer's move
        make_computer_move(board)
        print_board(board)
        if check_win(board, 'X'):
            print("Computer wins!")
            break
        if ' ' not in board:
            print("It's a draw!")
            break

# Start the game
play_game()