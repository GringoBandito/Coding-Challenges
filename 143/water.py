

def get_trapped_water(seq):
    """Input list of room heights
    Returns: Area of water between rooms"""
    
    assert isinstance(seq,list)
    for i in seq:
        assert isinstance(i,int) and i >= 0
        
    area = 0
    lst = []
    
    for i in range(len(seq)):
        
        while len(lst) != 0 and seq[lst[-1]] < seq[i]:
            
            height = seq[lst[-1]]
            lst.pop()
            
            if len(lst) == 0:
                break
            
            distance = i - lst[-1] - 1
            minendpoint = min(seq[lst[-1]], seq[i]) - height
            
            area += distance * minendpoint
            
        lst.append(i)
        
    return area



    