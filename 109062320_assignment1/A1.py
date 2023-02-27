#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np

def EnumerateAll(mlist, m, n):
    ''' Enumerate all the n-tuple from mlist.
        where mlist contains m numbers.
        We assume m >= n.
    ''' 

    # this is just for demo purpose.
    # write your own code for question (3) here.
    return [[0,1], [0,2], [1,2]];
    

def SolveLP(A, b, G):
    '''Solve the linear programming problem
        Max G(x)
        st. Ax <= b
             x >= 0
    '''
    # step 0: initialization
    maxg = 0;
    
    # step 1a: enumuate all combinations
    [m, n] = A.shape
    lst = EnumerateAll(np.arange(m), m, n)
    
    # step 1b: compute all the intersection points
    points = [];
    for idx in lst:
        Ai = A[idx, :]
        bi = b[idx]
        xi = np.linalg.solve(Ai, bi)
        
        # step 2: check the feasibility of the itersection point
        feasible = 1
        for i in range(m):
            if np.dot(A[i,:], xi) > b[i]:  # violate a constraints
                feasible = 0
        if feasible == 1:            # only add the feasible point
            points.append(xi)
        
    # step 3: evaluate the G function for all intersection points
    values = []
    for ptx in points:
        values.append(np.dot(G[0:n], ptx)+G[-1])
    
    # step 4: find the point with the largest value as the result
    maxg = max(values)
    maxidx = values.index(maxg)
    x = points[maxidx]
    
    return x, maxg
    
#-------------------------------#
# main program starts from here.#
#-------------------------------#
# Put all the coefficients of the constrains into a matrix A and a vector b

A = np.array([[1,1],[10,1],[2,14]])
b = np.array([6, 50, 40])
G = np.array([12, 15, 10])

# solve this problem
[x, maxg] = SolveLP(A, b, G)
print(x)
print(maxg)

