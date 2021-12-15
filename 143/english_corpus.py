
def write_chunks_of_five(words,fname):
    """Takes chunk of five words from 10000 most common english words
    and writes them together on a single line in seperate output file"""
    
    assert isinstance(words,list)
    assert isinstance(fname,str)
    
    count = 0
    
    with open(fname, 'w') as f:
        while count < len(words):
            
            sentence = " ".join(words[count:count+5])
            f.write(sentence + "\n")
            count += 5
    
    pass


