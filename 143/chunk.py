

def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''
    
    
    assert isinstance(n,int), "Number of chunks must be integer value"
    assert isinstance(fname,str), "Input file must be string"
    
    
    lst = []
    lst_len = []
    
    with open(fname) as f:
        for line in f:
            lst.append(line)
            lst_len.append(len(line))
    
    print(lst[0:5])
    total = []
    count = 0
    for i in lst_len:
        count += i
        total.append(count)
    
    size = total[-1]
    
    chunk = round(size/n)
    
    
    bounds = list(range(0,(n+1)*chunk,chunk))
    splits = [0]
    
    for i in bounds:
        for j in range(len(total)):
            
            if i <= total[j] and i > total[j-1]:
                bound = total[j-1]
                splits.append(total.index(bound) + 1)
                pass
    
    
        

    if bounds[-1] >= total[-1]:
        splits.append(total.index(total[-1]) + 1)
            
    
    
    
    
    for i in range(n):
        with open(fname + '_' + str(i).zfill(3) + '.txt', 'wt') as f:
            s = slice(splits[i],splits[i+1])
            f.writelines(lst[s])
            print(sum(lst_len[s]))
       
    return



                    
                    
