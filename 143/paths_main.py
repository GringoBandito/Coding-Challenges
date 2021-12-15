

def count_paths(m,n,blocks):
    """Inputs: m rows of grid 
    n: columns of grid
    blocks : blockages on path
    
    returns all possible paths from top left to bottom right of grid"""
    
    assert isinstance(m,int) and m > 0
    assert isinstance(n,int) and n > 0
    assert isinstance(blocks,list)
    for i in blocks:
        assert isinstance(i,tuple) and i[0] <= m-1 and i[1] <= n-1
        
    p = []
    num = []
        
    def findpaths(M,N,path,i,j):
        
        if i == M-1 and j == N-1:
            num.append(path + [i,j])
            return 
    
    
        path.append([i,j])
    
    
        if i + 1 <= M - 1 and j <= N-1:
            if (i+1,j) not in blocks:
                findpaths(M,N,path,i+1,j)
            
        if i <= M - 1 and j + 1 <= N-1:
            if (i,j+1) not in blocks:
                findpaths(M,N,path,i,j+1)
                
        path.pop()
        
    findpaths(m,n,p,0,0)
    
    
    return len(num)







                    
                    
            
        
    
          
    
    
        
        
    
    
    

        