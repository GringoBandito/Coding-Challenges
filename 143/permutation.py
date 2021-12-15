

def next_permutation(t:tuple) -> tuple:
    """Takes a tuple and returns next permutation in lexicogprahic order"""
    assert len(t) > 0
    assert isinstance(t,tuple)
    for i in t:
        assert isinstance(i,int) and i >= 0 
        
    
    
    t = list(t)
    
    if sorted(t,reverse=True) == list(t):
        return tuple(sorted(t))
    
    ind = 0
    ind2 = 0
    for i in range(len(t) - 1):
        if t[i+1] > t[i]:
            ind = i
            
    for j in range(len(t)):
        if t[j] > t[ind]:
            ind2 = j
        
    
    t[ind],t[ind2] = t[ind2],t[ind]
    
    lst = t[0:ind+1]
    lst2 = t[ind+1:]
    if len(lst2) > 1:
        lst2.reverse()
        
    
    final = lst + lst2
    
    return tuple(final)







