import generate_boards as gb
import boards


'''
pre_X = [[[0,0,0],[0,0,0],[0,0,0]]]

X = gb.Make_X(pre_X,1) #<- to be fixed (its inverted)
Y = gb.Make_y(X,-1)
gb.record_file('X.txt',str(X))
gb.record_file('Y.txt',str(Y))
'''
#---------------------------------------
def get_num_option(X_pre,pos,player):
	"""
	"""
	#HUMAN = -1
	#COMP = +1
	#player = HUMAN
	X = [gb.split_3_lists(l) for l in X_pre]#adaptor
	depth = X[pos].count(0)+X[pos][1].count(0)+X[pos][2].count(0)
	best_minimax = gb.minimax(X[pos], depth, player)
	call_possible_turns = gb.possible_turns(X[pos], player)

	#moving by minimax:
	xx, yy = best_minimax[:2]
	MOVE = gb.set_move(xx, yy, player, X[pos]) #TRUE OR FALSE
	if MOVE == True:
		X[pos][xx][yy]=player
	else:
		#print('ERROR!')
		num_turn_option = 0
		return num_turn_option
	#---
	#Get num of turn option:
	for i in range(len(call_possible_turns)):
		if call_possible_turns[i] == X[pos]:
			num_turn_option = i + 1
	#---
	'''
	print(X[pos]) #minimax's best = [0, 0, -1]
	print(call_possible_turns) #[[[1, 0, 1], [-1, -1, 0], [1, 0, -1]], [[0, 1, 1], [-1, -1, 0], [1, 0, -1]], [[0, 0, 1], [-1, -1, 1], [1, 0, -1]], [[0, 0, 1], [-1, -1, 0], [1, 1, -1]]]
	print(num_turn_option)
	'''
	return(num_turn_option)
'''
HUMAN = -1
COMP = +1
player = COMP
X=boards.X
'''
#Y = gb.Make_y(X)

#pos = () -1 #2023 -> [[0, 0, 1], [-1, -1, 0], [1, 0, -1]]
#print(X[pos])#DEBUG

def Make_y(X):
	"""Makes marks which option  did minimax choose to play \n
    	0 -none; 1-9 position from left to right
    	Requiers: X_all (all boards)
    """
	HUMAN = -1
	COMP = +1
	#Y = [get_num_option(X,step) for step in range(len(X))] #old
	Y = []
	for step in range(len(X)):
		if X.count(1)-X.count(-1) == 1 or X.count(1)-X.count(-1) == 0:
			Y.append(get_num_option(X,step,HUMAN))

		elif X.count(1)-X.count(-1) == -1:
			Y.append(get_num_option(X,step,COMP))

	return Y

import boards 
Y = Make_y(boards.X_all)
gb.record_file('Y.txt',str(Y))

#For ALL POSSIBLE BOARS (HUMAN nad COMP):

def ALL_BOARDS():
	"""For ALL POSSIBLE BOARS (HUMAN nad COMP)
		Requires: generate_boards.py
		Ensures: ALL BOARDS as X_all
	"""
	X_all = gb.get_all_boads()#all of then

	X_all2 = [gb.split_3_lists(l) for l in X_all]#adaptor

	X_all = gb.filter(X_all2)#Cheater boards are removed
	return X_all
