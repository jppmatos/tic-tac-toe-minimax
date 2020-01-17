from gplearn.genetic import SymbolicRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.utils.random import check_random_state
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import graphviz

from gplearn.functions import make_function
from gplearn.fitness import make_fitness

#x0 = 1+2+2+2+1
#x1 = 5

#y_truth = x0 / x1# = 1.6


rng = check_random_state(0)

# Training samples
#X_train = rng.uniform(-1, 1, 100).reshape(50, 2)
#y_train = X_train[:, 0] / X_train[:, 1]

X_train = [[4,2],[24,3]]
y_train = [2,8]

# Testing samples
#X_test = rng.uniform(-1, 1, 100).reshape(50, 2)
#y_test = X_test[:, 0] / X_test[:, 1]

#Custom Functions:
'''
def _logical(x1, x2, x3, x4):
    print('x1:',x1)
    #print('x2:',x2)
    #print('x3:',x3)
    print('x4:',x4)
    print('::',np.where(x1 > x2, x3, x4))
    return np.where(x1 > x2, x3, x4)
'''
def _logical(x1,x2):
    print('x1:',x1)
    print('x2:',x2,'\n')

    for i in range (len(x1)):
      xx = []
      xx.append(x1[i])
      xx.append(x2[i])
      #print(xx,'\n')

   
    print(np.shape(np.array(x1)))
    return np.array(x1)
#
logical = make_function(function=_logical,
                        name='logical',
                        arity=2)
#
#Custom Fitness:
def _mape(y, y_pred, w):
    """Calculate the mean absolute percentage error."""
    #print('y_fit:',y)#DEBUG
    #print('y_pred_fit:',y_pred)#DEBUG
    diffs = np.abs(np.divide((np.maximum(0.001, y) - np.maximum(0.001, y_pred)),
                             np.maximum(0.001, y)))
    #print('Fit:',100. * np.average(diffs, weights=w))
    return 100. * np.average(diffs, weights=w)
mape = make_fitness(_mape, greater_is_better=False)
#
est_gp = SymbolicRegressor(metric=mape,function_set=['add', 'sub', 'mul', 'div',logical], population_size=4,
                           generations=2, stopping_criteria=0.01,
                           p_crossover=0.7, p_subtree_mutation=0,
                           p_hoist_mutation=0, p_point_mutation=0,
                           max_samples=0.9, verbose=1,
                           parsimony_coefficient=0.01, n_jobs = 4)#, random_state=10)

print(est_gp.fit(X_train, y_train))

#print(est_gp._program)
'''
    |   Population Average    |             Best Individual              |
---- ------------------------- ------------------------------------------ ----------
 Gen   Length          Fitness   Length          Fitness      OOB Fitness  Time Left
   0    35.92          334.775       11         0.756994          1.10215      4.02s
   1    10.68          2.34371       11                0                0      2.36s
div(add(mul(sub(X0, X1), sub(X1, X1)), X0), X1)
div(add(mul(sub(X0, X1), sub(X1, X1)), X0), X1)
[Finished in 1.8s]
'''
#print(est_gp.get_params)
'''
<bound method BaseEstimator.get_params of SymbolicRegressor(const_range=(-1.0, 1.0), feature_names=None,
                  function_set=('add', 'sub', 'mul', 'div'), generations=50,
                  init_depth=(2, 6), init_method='half and half',
                  low_memory=False, max_samples=0.9,
                # metric='mean absolute error', n_jobs=1, p_crossover=0.7, #
                  p_hoist_mutation=0.05, p_point_mutation=0.1,
                  p_point_replace=0.05, p_subtree_mutation=0.1,
                  parsimony_coefficient=0.01, population_size=120,
                  random_state=10, stopping_criteria=0.01, tournament_size=20,
                  verbose=1, warm_start=False)>
'''