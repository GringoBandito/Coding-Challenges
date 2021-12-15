

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
