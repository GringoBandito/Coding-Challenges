import pandas as pd
from datetime import date, datetime, time



def add_month_yr(x):
    '''Takes dataframe x and adds column of month-year based on timestamp'''
    
    assert isinstance(x,pd.DataFrame)
    
    x['month-yr'] = pd.to_datetime(x['Timestamp']).apply(lambda i: i.strftime('%b-%Y'))
    
    return x



def fix_categorical(x):
    '''Takes dataframe with month-year and returns dataframe of count of each month 
    year combo'''
    
    assert isinstance(x,pd.DataFrame)
    
    
    df = x.groupby('month-yr')['Timestamp'].count()
    df = pd.DataFrame(df)
    
    lst = list(df.index.values)
    lst.sort(key = lambda d: datetime.strptime(d,'%b-%Y'))
    
    
    x['month-yr'] = pd.Categorical(x['month-yr'], categories = lst, ordered=True)
    
    
    return x

