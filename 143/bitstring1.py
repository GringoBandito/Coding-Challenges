import numpy as np


def get_sample(nbits=3,prob=None,n=1):
    """Takes inputs a number of bits and probability mass function and returns
    A list of length n of that sample"""
    
    assert isinstance(nbits,int) and nbits > 0
    assert isinstance(prob,dict) and len(prob) > 0 and len(prob)<= 2**nbits
    assert isinstance(n,int) and n > 0
    
    probability = 0
    
    for bits in prob.keys():
        assert len(bits) == nbits
        if len(prob) == 1:
            assert isinstance(prob[bits],int) or isinstance(prob[bits],float)
        
               
        probability += prob[bits]
    
    assert probability == 1
    
    key = list(prob.keys())
    probs = list(prob.values())
    
    return (list(np.random.choice(key,n,probs)))

