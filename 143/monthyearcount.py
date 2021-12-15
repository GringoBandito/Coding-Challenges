import pandas as pd



def add_month_yr(x):
    '''Takes dataframe x and adds column of month-year based on timestamp'''
    
    assert isinstance(x,pd.DataFrame)
    
    x['month-yr'] = pd.to_datetime(x['Timestamp']).apply(lambda i: i.strftime('%b-%Y'))
    
    return x



def count_month_yr(x):
    '''Takes dataframe with month-year and returns dataframe of count of each month 
    year combo'''
    
    assert isinstance(x,pd.DataFrame)
    
    df = x.groupby('month-yr').size()
    df = pd.DataFrame(df)
    
    return df

