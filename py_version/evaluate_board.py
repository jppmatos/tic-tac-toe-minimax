#--------------paths_count-----------------------
def count_paths_1(state,player):
    '''
    Counts possible paths wtih 0 space with the player and 3 empty spaces 
    '''
    #player = -1 # 1
    opponent = player * (-1)
    player = str(player)
    opponent = str(opponent)
    solutions = ['0'+'0'+'0']#dif_solutions
    counts = 0
    #vertical 
    for x in range(3):
        note = ''
        for y in range(3):
            note += str(state[y][x])
        if note in solutions:
            counts+=1
    #horizontal 
    for x in range(3):
        note = ''
        for y in range(3):
            note += str(state[x][y])
        if note in solutions:
            counts+=1
    #diagonal
    if str(state[0][0])+str(state[1][1])+str(state[2][2]) in solutions or str(state[0][2])+str(state[1][1])+str(state[2][0]) in solutions:
        counts+=1
    return counts 
def count_paths_2(state,player):
    '''
    Counts possible paths wtih 1 space with the player and 2 empty spaces 
    '''
    #player = -1 # 1
    opponent = player * (-1)
    player = str(player)
    opponent = str(opponent)
    solutions = [player+'0'+'0','0'+player+'0','0'+'0'+player]#dif_solutions
    counts = 0
    #vertical 
    for x in range(3):
        note = ''
        for y in range(3):
            note += str(state[y][x])
        if note in solutions:
            counts+=1
    #horizontal 
    for x in range(3):
        note = ''
        for y in range(3):
            note += str(state[x][y])
        if note in solutions:
            counts+=1
    #diagonal
    if str(state[0][0])+str(state[1][1])+str(state[2][2]) in solutions or str(state[0][2])+str(state[1][1])+str(state[2][0]) in solutions:
        counts+=1
    return counts 

def count_paths_3(state,player):
    '''
    Counts possible paths wtih 2 spaces with the player and 1 empty space 
    '''
    #player = -1 # 1
    opponent = player * (-1)
    player = str(player)
    opponent = str(opponent)
    solutions = [player+player+'0' ,player+'0'+player, player+player+'0']#dif_solutions
    counts = 0
    #vertical 
    for x in range(3):
        note = ''
        for y in range(3):
            note += str(state[y][x])
        if note in solutions:
            counts+=1
    #horizontal 
    for x in range(3):
        note = ''
        for y in range(3):
            note += str(state[x][y])
        if note in solutions:
            counts+=1
    #diagonal
    if str(state[0][0])+str(state[1][1])+str(state[2][2]) in solutions or str(state[0][2])+str(state[1][1])+str(state[2][0]) in solutions:
        counts+=1
    return counts 

#Testing
'''
board = [
    [0, 0, -1],
    [0, -1, +1],
    [+1, 0, 0],
]
print('Points_1_paths: ',count_paths_1(board,-1))
print('Points_2_paths: ',count_paths_1(board,-1))
print('Points_3_paths: ',count_paths_2(board,-1))
'''
#---
def getMAX_list_Y(l):
    """
    """
    y_max = l.index(max(l))
    return y_max
