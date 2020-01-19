from math import inf as infinity
from random import choice
import platform
import time
from os import system
import itertools
from copy import deepcopy
#GLOBAL VARs:
HUMAN = -1 
COMP = +1
#
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
    :param state: the state of the current board = turn
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells
#-------------------------------------------------------------------------
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
#-------------------------------------------------------------------------
def valid_move(x, y, board):
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

def set_move(x, y, player, board):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y, board):
        board[x][y] = player
        #print(board[x][y])#DEBUG
        return True
    else:
        return False

def minimax(state, depth, player): #(start_board,depth,start_player)
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

    if depth == 0 or game_over(state):#
        score = evaluate(state)#who won 
        return [-1, -1, score]

    for cell in empty_cells(state):#
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)#eval_state_new(state,player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best
#---------_--_-_-___-------__----------------------
def ai_turn(turn,depth):#def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))#
    #print('depth',depth)#DEBUG
    if depth == 0 or game_over(board):
        return

    #clean()
    print(f'Computer turn [{c_choice}]')
    #
    draw_board(turn)#
    #render(board, c_choice, h_choice)
    #
    if depth == 9: #< - end game?
        x = choice([0, 1, 2]) # 0 or 1 or 2
        y = choice([0, 1, 2])
    else: # < - minimax!
        move = minimax(board, depth, COMP)
        #print('move_minimax: ',move)#DEGUB
        #move = [1, 1, 0]
        x, y = move[0], move[1] 
    #
    p_t = player_turn('o', p_t[move-1])#(start_player, p_t[joystick])
    return p_t
    #set_move(x, y, COMP) #< - make the move

    time.sleep(1)
#-----------------------------------------------------------------------------

def merge_3_lists(l):
    """Merge a list of 3 lits with 3 itens l into a single lits new_l"""
    new_l = [j for i in l for j in i]
    return new_l

def split_3_lists(l):
	"""Split a list l into a list of 3 lits with 3 itens new_l"""
	new_l = [l[i:i+3] for i in range(0, len(l), 3)]
	return new_l

def get_all_boads():
	"""Gets all possible boads of a end of a game
		Requires: itertools for the generation of all possible statess
		Ensures: returns X as the list of all states in lists
	"""
	x = [-1,0,1] #[-1,0,1]
	v = [p for p in itertools.product(x, repeat=9)]
	#Ensures that aren't any cheating boards:
	X = [list(item) for item in v if item.count(-1)<=5 and item.count(1)<=5]
	#converts to the 3_lists format:
	
	return X

def possible_turns(n_turn,player):
    """Verifies possible turns
        Requires: turn to be dict and player to be a str
        Ensures: list of possibles turns as p_turns_list"""
    p_turns_list=[]
    for i in range(0, 3):
        new_turn = deepcopy(n_turn)
        for j in range(0, 3):
            new_turn = deepcopy(n_turn)
            #
            if (n_turn[i][j] == 0):
                new_turn[i][j] = player#problem
                p_turns_list.append(new_turn)  
    return(p_turns_list)

def record_file(file_name,content):
    """Makes .txt <file from content>
    """
    out_file = open(file_name,'w')
    out_file.write(content)
    out_file.close()
#----------------------------------------------
def filter(X):#<- to be fixed (its inverted)
    """Filters cheater boards by the difference between <-1> s and <1> that is between [-1,0] \n
         you only have the boards where player -1 started
    """
    f_X = []
    for f in X:
        f_m = merge_3_lists(f)
        if f_m.count(1)-f_m.count(-1) == -1 or f_m.count(1)-f_m.count(-1) == 0 or f_m.count(1)-f_m.count(-1) == 1: #or f_m.count(1)-f_m.count(-1) ==1:
            f_X.append(split_3_lists(f_m))
    
    return f_X

def Make_X(X,player):# Not being used!
    """Makes all the possible boards , list of lists
    """
    for p in X:
        if wins(p,player*(-1)) != player*(-1):

            t=possible_turns(p,player)#lista de possibilidades
          
            for sub_t in t:
                if sub_t not in X:
                    X.append(sub_t)

                    if wins(sub_t,player) != player:
                        t=possible_turns(p,player*(-1))
                        for sub_t in t:
                            if sub_t not in X:
                                X.append(sub_t)

                               
    X = filter(X)
    return X

#---------------------------------------
def get_num_option(X,pos,player):
    """get the total of all possible options and then selects the one form minimax's
        Requires:X <list of lists> for for the board, pos <int> position on the X list of lists, player <int> HUMAN = -1 or COMP = +1
        Ensures: returns num_turn_option <int> the turn option
        player = HUMAN
    """
    depth = X[pos][0].count(0)+X[pos][1].count(0)+X[pos][2].count(0)
    best_minimax = minimax(X[pos], depth, player)
    call_possible_turns = possible_turns(X[pos], player)

    #moving by minimax:
    xx, yy = best_minimax[:2]
    MOVE = set_move(xx, yy, player, X[pos]) #TRUE OR FALSE
    if MOVE == True:
        X[pos][xx][yy]=player
    else:
        num_turn_option = 0
        return num_turn_option
    #Get num of turn option:
    for i in range(len(call_possible_turns)):
        if call_possible_turns[i] == X[pos]:
            num_turn_option = i + 1

    return(num_turn_option)

def Make_y(X,player):
    """Makes marks which option  did minimax choose to play \n
        0 -none; 1-9 position from left to right
        player is -1(HUMAN) or 1(COMP)
    """
    Y = [get_num_option(X,step,player) for step in range(len(X))]
    return Y
