#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)
"""

'''
HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
'''

def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    #state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best#score - save?


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(state, c_choice, h_choice):
    """
    Print the board on console
    :param state: current state of the board
    """
    
    #render [[0, 0, 0], [0, 0, 0], [0, 0, 0]] O X

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'
    print('render',state, c_choice, h_choice)#DEBUG
    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    print('depth',depth)#DEBUG
    if depth == 0 or game_over(board):
        return

    #clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 9: #< - end game?
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else: # < - minimax!
        move = minimax(board, depth, COMP)
        print('move_minimax: ',move)#DEGUB
        x, y = move[0], move[1]

    set_move(x, y, COMP) #< - make the move
    time.sleep(1)

def ai_turn_h(h_choice, c_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    print('depth',depth)#DEBUG
    if depth == 0 or game_over(board):
        return

    #clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 9: #< - end game?
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else: # < - minimax!
        move = minimax(board, depth, HUMAN)#changed
        print('move_minimax: ',move)#DEGUB
        x, y = move[0], move[1]

    set_move(x, y, HUMAN) #< - make the move #changed
    time.sleep(1)
def human_turn(c_choice, h_choice):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    #clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main(start):
    """
    Main function that calls all functions
    """

    #clean()
    h_choice = 'X'  # X or O
    c_choice = 'O'  # X or O
    first = start  # if h_choice (human) is the first

    #clean()

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        #print('board:', board)
        if first == 'N':
            print('robo-comp: ',c_choice)
            ai_turn(c_choice, h_choice)
            #print('board:', board)
            first = ''
        #
        print('robo-human: ',h_choice) #first gap!!!
        ai_turn_h(h_choice, c_choice)
        #print('board:', board)
        #human_turn(c_choice, h_choice)
        print('robo-comp: ',c_choice)
        ai_turn(c_choice, h_choice)
        #print('board:', board)

    # Game over message
    if wins(board, HUMAN):
        #clean()
        print(f'Computer turn [{h_choice}]','end')
        #print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        #print('board:', board)
        print(f'YOU WIN! [{h_choice}]')
    elif wins(board, COMP):
        #clean()
        print(f'Computer turn [{c_choice}]','end')
        #print('board:', board)
        render(board, c_choice, h_choice)
        print(f'YOU LOSE! [{c_choice}]')
    else:
        #clean()
        render(board, c_choice, h_choice)
        #print('board:', board)
        print('DRAW!')

    exit()

HUMAN = -1 #"X"
COMP = +1 #"O"
'''
board = [
    [0, 0, -1],
    [0, -1, +1],
    [+1, 0, 0],
]
'''
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

start_player = 'Y' #'X' or 'O'
if start_player =='X':
    start = 'Y'
else:
    start = 'N'


if __name__ == '__main__':
    main(start)
