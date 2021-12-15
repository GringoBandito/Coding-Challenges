
def write_columns(data,fname):
    """Writes each data value in data to file=fname in following fashion:
        data_value, data_value**2, (data_value+data_value**2)/3"""
        
    assert isinstance(data,list)
    assert isinstance(fname,str)
        
    with open(fname, 'w') as f:
        for i in data:
            value1 = round(i,2)
            value2 = round(i*i,2)
            value3 = round((i+i**2)/3,2)
            f.write('%3.2f, %3.2f, %3.2f \n' %(value1,value2,value3))
        
    pass

