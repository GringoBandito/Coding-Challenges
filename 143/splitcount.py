import pandas as pd


def split_count(x):
    '''Takes pandas series of categorical variables and returns dataframe of counts'''
    
    assert isinstance(x,pd.Series)
    for char in x:
        assert isinstance(char,str)
    
    d = dict()
    
    for i in x:
        i = i.split(',')
        
        for j in i:
            j = j.strip()
            if j in d.keys():
                d[j] += 1
            
            else:
                d[j] = 1
                
    df = pd.DataFrame.from_dict(d,orient='index')
    
    return df

