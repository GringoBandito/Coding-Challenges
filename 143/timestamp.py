import pandas as pd




def add_month_yr(x):
    '''Takes dataframe x and adds column of month-year based on timestamp'''
    
    assert isinstance(x,pd.DataFrame)
    
    x['month-yr'] = pd.to_datetime(x['Timestamp']).apply(lambda i: i.strftime('%b-%Y'))
    
    return x



