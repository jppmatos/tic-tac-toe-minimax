from gplearn.genetic import SymbolicRegressor
from gplearn.fitness import make_fitness
from gplearn.functions import make_function

from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.utils.random import check_random_state
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
##
from math import inf as infinity
from random import choice
import platform
import time
from os import system

import pickle
##
import generate_boards as gb
import evaluate_board as eb
import boards


#Global varialbles:
HUMAN = -1 #"X"
COMP = +1

state = [
    [0, 0, -1],
    [0, -1, +1],
    [+1, 0, 0],
]
depth = 0
player =HUMAN #gp

dummy = np.arange(10)

#-----------------
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
#----
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
        score = evaluate(state)#
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
#_______________|GPlearn|__________________
# Training samples
#X_train: Training vectors, where n_samples is the number of samples and n_features is the number of features.
#X_train = [[0, 0, -1, 0, -1, 1, 1, 0, 0],[0, 0, -1, 0, -1, 1, 1, 0, 0],[0, 0, -1, 0, -1, 1, 1, 0, 0]]
#y_train = [1,0,2] # Target values.
X_train = boards.X_all
y_train = boards.Y_all

def _fitover(y, y_pred, w):
    '''
    test:
    <y> is the input target y vector, (the actual target values)
    <y_pred> is the predicted values from the genetic program, (the predicted values from the program) 
    <sample_weight> is the sample_weight vector.  (the weights to apply to each sample) 
    '''
    if len(y_pred) == 2:# because of the inicial y_pred ([2 2])
        return 2
 
    HUMAN = -1 
    COMP = +1
    X_raw = X_train
    
    score_fit = 0
    for pos in range(len(y_pred)):
        #plays as who?
        if X_raw[pos].count(1)-X_raw[pos].count(-1) == 1 or X_raw[pos].count(1)-X_raw[pos].count(-1) == 0:
            player = HUMAN
        elif X_raw[pos].count(1)-X_raw[pos].count(-1) == -1:
            player = COMP

        X_pros = gb.split_3_lists(X_raw[pos])#adaptor
        call_possible_turns = gb.possible_turns(X_pros, player)
        lista_y = [0]
        for pre_ind in call_possible_turns:
            ind = gb.merge_3_lists(pre_ind)
            num = 0
  
            while ind != X_raw[num]:
                #print('X_raw[num]',X_raw[num])#DEBUG
                num += 1
            lista_y.append(y_pred[num])
            #print('||>',num,'\n')

        max_val_lista = max(lista_y)
        y_max = lista_y.index(max_val_lista) #<= getMAX_list_Y(lista_y) # = lista_y.index(max(lista_y)) #: returns the position of the maximum element of list_y.
        predicted_pos = y_max# posição onde encontro o y_max em lista_y
        if y[pos] == predicted_pos:
            score_fit += 0.1 
 
    return score_fit

fitover = make_fitness(_fitover, greater_is_better=True,wrap=True)# voltar a _> greater_is_betterstoping_criteria=True
def _count_paths_1(X0,X1,X2,X3,X4,X5,X6,X7,X8):
    '''
    Counts possible paths wtih 1 space of the player 
    '''
    list_of_scores = []
    for i in range (len(X0)):
        score_step = 0
        stats_step = []
        stats_step.extend([X0[i],X1[i],X2[i],X3[i],X4[i],X5[i],X6[i],X7[i],X7[i],X8[i]])
        
        if stats_step.count(1)-stats_step.count(-1) == 1 or stats_step.count(1)-stats_step.count(-1) == 0:
            score_step += eb.count_paths_1(gb.split_3_lists(stats_step),HUMAN)

        elif stats_step.count(1)-stats_step.count(-1) == -1:
            score_step += eb.count_paths_1(gb.split_3_lists(stats_step),COMP)

        list_of_scores.append(score_step)

    return np.array(list_of_scores) 

def _count_paths_2(X0,X1,X2,X3,X4,X5,X6,X7,X8):
    '''
    Counts possible paths wtih 2 space of the player 
    '''
    #print(np.shape(X0)) #(8953,)
    #print('Xs:')
    #print(X0)
    #print(X1)
    #print(X2)
    #print(X3)
    #print(X4)
    #print(X5)
    #print(X6)
    #print(X7)
    #print(X8)
    #print('\n')
    list_of_scores = []
    for i in range (len(X0)):
        score_step = 0
        stats_step = []
        stats_step.extend([X0[i],X1[i],X2[i],X3[i],X4[i],X5[i],X6[i],X7[i],X7[i],X8[i]])
        
        if stats_step.count(1)-stats_step.count(-1) == 1 or stats_step.count(1)-stats_step.count(-1) == 0:
            score_step += eb.count_paths_2(gb.split_3_lists(stats_step),HUMAN)

        elif stats_step.count(1)-stats_step.count(-1) == -1:
            score_step += eb.count_paths_2(gb.split_3_lists(stats_step),COMP)

        list_of_scores.append(score_step)

    return np.array(list_of_scores)

def _count_paths_3(X0,X1,X2,X3,X4,X5,X6,X7,X8):
    '''
    Counts possible paths wtih 1 space of the player 
    '''
    list_of_scores = []
    for i in range (len(X0)):
        score_step = 0
        stats_step = []
        stats_step.extend([X0[i],X1[i],X2[i],X3[i],X4[i],X5[i],X6[i],X7[i],X7[i],X8[i]])
        
        if stats_step.count(1)-stats_step.count(-1) == 1 or stats_step.count(1)-stats_step.count(-1) == 0:
            score_step += eb.count_paths_3(gb.split_3_lists(stats_step),HUMAN)

        elif stats_step.count(1)-stats_step.count(-1) == -1:
            score_step += eb.count_paths_3(gb.split_3_lists(stats_step),COMP)

        list_of_scores.append(score_step)

    return np.array(list_of_scores) 

#factory function:
count_1 = make_function(function=_count_paths_1,
                        name='count_1',
                        arity=9)
count_2 = make_function(function=_count_paths_2,
                        name='count_2',
                        arity=9)
count_3 = make_function(function=_count_paths_3,
                        name='count_3',
                        arity=9)

est_gp = SymbolicRegressor(metric=fitover,
                            function_set=[count_1,count_2,count_3,'add', 'sub', 'mul', 'div'],
                            population_size=20,#10
                            generations=60,#20
                            stopping_criteria=10000,
                            p_crossover=0.7, p_subtree_mutation=0.01,
                            p_hoist_mutation=0.01, p_point_mutation=0.01,
                            max_samples=0.9, verbose=1,
                            parsimony_coefficient=0.01,const_range=(-1,1),
                            n_jobs=-1)

#
print(est_gp.fit(X_train, y_train))

print(est_gp._program)

'''
dot_data = est_gp._program.export_graphviz()
graph = graphviz.Source(dot_data)
graph
'''


#print('predict: ',est_gp.predict([[-1, -1, 1, 1, -1, 0, -1, 1, 0]])) #ver se há troca de jogador?


def save_programe(gp_model,name):
    """Save gp_model ou programe
        Reuires: gp_model vaiable name, name <str> of the savefile
        Ensures: .pkl file with the saved programe
    """
    f = open(name+'.pkl', 'wb')
    pickle.dump(gp_model, f)
    f.close()




save_programe(est_gp,'est_gp_model')
#print(est_gp.get_params)

'''
from IPython.display import Image
import pydotplus
graph = est_gp._program.export_graphviz()
graph = pydotplus.graphviz.graph_from_dot_data(graph)
Image(graph.create_png())
'''
'''
est_gp = SymbolicRegressor(metric=fitover,
                            function_set=[count_1,count_2,count_3,'add', 'sub', 'mul', 'div'],
                            population_size=40,
                            generations=80, 
                            stopping_criteria=10000,
                            p_crossover=0.7, p_subtree_mutation=0.01,
                            p_hoist_mutation=0.01, p_point_mutation=0.01,
                            verbose=1,
                            parsimony_coefficient=0.01,
                            n_jobs=-1)
'''