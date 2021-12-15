import numpy as np


        
def gen_rand_slash(m=6,n=6,direction='back'):
    """Takes length and width of a box and returns a random slash forward or backward
    depending on direction"""
    assert isinstance(m,int) and m >= 2
    assert isinstance(n,int) and n >= 2
    assert isinstance(direction,str) and direction.lower() in ['back','forward']
    
    lst = []
    lst2 = []
    count = 1
    ind = 2
    while count < max(m,n) - 1:
        vec=np.zeros((m,n))
        for i in range(m - count):
            for j in range(n - count):
                for k in range(ind):
                    vec[i+k][j+k] = 1
                
                lst.append(vec)
                vec = np.zeros((m,n))
                
        vec=np.zeros((m,n))
        
        
        
        count += 1
        ind += 1
    
    if m == n:
        elf = np.eye(m)
        lst.append(elf)
        
                
    for i in lst:
        test = i
        lst2.append(test[:,::-1])
    
    
    if direction == 'back':
        numb = np.random.randint(0,len(lst))
        return lst[numb]
    
    numb = np.random.randint(0,len(lst2))
    return lst2[numb]



                