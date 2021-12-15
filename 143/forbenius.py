import numpy as np
import math 
import itertools as it

def solvefrob(coefs,b):
    """Inputs: coefs - list of coefficients 
        b - integer 
        
        return: x - solution to ax = b
        
        a,b > 0 and x>= 0"""
        
    assert isinstance(coefs,list)
    for i in coefs:
        assert isinstance(i,int) and i > 0 
        
    assert isinstance(b,int) and b > 0
    
    
    lst = []
    lst2 = []
    lst3 = []
    
    for i in coefs:
        c= math.ceil(b/i)
        lst.append(np.arange(c+1))
        
    for comb in it.product(*lst):
        lst2.append(comb)
        
    for p in lst2:
        p = np.array(p)
        test = np.dot(p,np.array(coefs))
        if test == b:
            lst3.append(tuple(p))
    
    return lst3


    
