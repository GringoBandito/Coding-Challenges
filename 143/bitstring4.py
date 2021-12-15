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

def map_bitstring(instrings):
    """Takes list of bitstrings and returns dictionary where each bitstring is key
    and value is 1 if number of ones exceeds 0s in bitstring"""
    
    assert isinstance(instrings,list) and len(instrings) > 0
    for string in instrings:
        numb = len(string)
        assert isinstance(string,str)
        assert numb > 0
        assert len(string) == len(instrings[0])
        for i in string:
            assert i == '1' or i == '0'
            
    d = dict()
    
    for s in instrings:
        zero = 0
        one = 0
        
        for i in range(len(s)):
            if s[i] == '1':
                one += 1
            
            else:
                zero += 1
        if s not in d.keys() and zero > one:
            d[s] = 0
        
        if s not in d.keys() and zero <= one:
            d[s] = 1
    
    return d

def gather_values(seq):
    """Builds a dictionary with bitsrings as keys and values as lists corresponding to
    lists generated from map_bitstrings"""
    
    assert isinstance(seq,list) and len(seq) > 0
    for i in seq:
        assert isinstance(i,str) and len(i) > 0 and len(i) == len(seq[0])
        for j in i:
            assert j =='1' or j =='0'

    
    d1 = map_bitstring(seq)
    d2 = dict()
    
    for key1, value1 in d1.items():
        lst2 = []
        numb = 0
        for s in seq:
            if s == key1:
                numb += 1
            
        if key1 not in d2:
            if value1 == 1:
                for i in range(numb):
                    lst2.append(1)
                
                d2[key1] = lst2
            
            elif value1 == 0:
                for i in range(numb):
                    lst2.append(0)
            
                d2[key1] = lst2
    
    return d2

def threshold_values(seq,threshold=1):
    """Takes as input dictionary from gather_values and returns dictionary of 1 
    for bitstrings with most ones and zeros for bitstrings below threshold ranking"""
    
    assert isinstance(seq,list) and len(seq) > 0
    for i in seq:
        assert isinstance(i,str)
        assert len(i) > 0 and len(i) == len(seq[0])
        for j in i:
            assert j == '1' or j == '0'
    
    assert isinstance(threshold,int) and threshold > 0 and threshold <= 2**len(seq[1])
    
    
    totals = gather_values(seq)
    
    for i in totals.keys():
        totals[i] = totals.get(i).count(1)
    
   
    
    d = dict(sorted(totals.items(), key = lambda x:x[1], reverse=True))
    
    for j in d.keys():
        threshold -= 1
        if d[j] != 0:
            if threshold >= 0:
                d[j] = 1
            
            else:
                d[j] = 0

    return d
