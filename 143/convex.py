import numpy as np
from collections import Iterable 


def find_convex_cover(pvertices,clist):
    '''Inputs: pvertices = n-1 long iterable of polygon vertices
    clist = list of x,y tuples of circle centers
    
    output: array of m radii corresponding to m circle centers'''
    
    assert isinstance(clist, list)
    for i in clist:
        assert isinstance(i,tuple)
        for j in i:
            assert isinstance(j,float)
            
    assert isinstance(pvertices,Iterable)
    
    lst = []
    
    for center in clist:
        c1 = np.array(center)
        d = 100000
        for vertice in pvertices:
            v1 = np.array(vertice)
            dist = np.linalg.norm(v1 - c1)
            
            if dist <= d:
                d = dist
        
        
        if d!= 100000 :       
            lst.append(d)
            
    
    return lst

