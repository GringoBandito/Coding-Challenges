

def multinomial_sample(n,p,k=1):
    
    '''
    Return samples from a multinomial distribution.
    
    n:= number of trials
    p:= list of probabilities
    k:= number of desired samples
    '''
    from random import choices               
    assert isinstance(n,int) and n > 0
    assert isinstance(p,list)
    for i in p:
        assert isinstance(i,int) or isinstance(i,float)
        assert i >=0 and i <= 1
    assert sum(p) == 1
    assert isinstance(k,int) and k > 0
    
    
    lst = []
    count = 0
    
    while count < k:
        
        results = [0] * len(p)
        pop = [d for d in range(len(p))]
        
        sample = choices(pop, weights = p, k=n)
        
        for i in sample:
            results[i] +=1
        
        lst.append(results)
        count+=1
    
    
    
    return lst



