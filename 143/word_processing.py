

def get_average_word_length(words):
    """Takes a list of words and returns average length of words in list"""
    assert isinstance(words,list) and len(words) > 0
    for i in words:
        assert isinstance(i,str) and len(i) > 0 and i.isalpha()
    
    total = 0
    for i in words:
        total += len(i)
    
    return total/len(words)



def get_longest_word(words):
    """Input: List of words
    Output: Longest word in list"""
    assert isinstance(words, list) and len(words) > 0
    for i in words:
        assert isinstance(i,str) and len(i) > 0 and i.isalpha()
    
    top = 0
    word = ''
    
    for i in words:
        if len(i) > top:
            top = len(i)
            word = i
    
    return word

def get_longest_words_startswith(words,start):
    """Inputs: words - list of string of words
    start - str, letter of alphabet
    Output: Words with longest length starting with letter 'start' """
    assert isinstance(words,list) and len(words) > 0
    assert isinstance(start,str) and start.isalpha()
    for i in words:
        assert isinstance(i,str) and len(i) > 0 and i.isalpha()
  
    lst = []
    
    for i in words:
        if i[0] == start:
            lst.append(i)
            
    return get_longest_word(lst)


def get_most_common_start(words):
    """Takes list of words and returns string of most common starting letter"""
    assert isinstance(words, list) and len(words) > 0
    for i in words:
        assert isinstance(i,str) and len(i) > 0 and i.isalpha()
    
    d = dict()
    s = 'abcdefghijklmnopqrstuvwxyz'
    top = 0
    char = ''
    
    for i in s:
        d[i] = 0
        
    for j in words: 
        letter = j[0]
        d[letter] += 1
    
    for key in d:
        if d[key] > top:
            char = key
            top = d[key]
        
    return char


def get_most_common_end(words):
    """Takes list of words and returns string of most common ending letter in list of strings"""
    assert isinstance(words, list) and len(words) > 0
    for i in words:
        assert isinstance(i,str) and len(i) > 0 and i.isalpha()
    
    d = dict()
    s = 'abcdefghijklmnopqrstuvwxyz'
    top = 0
    char = ''
    
    for i in s:
        d[i] = 0
        
    for j in words: 
        letter = j[-1]
        d[letter] += 1
    
    for key in d:
        if d[key] > top:
            char = key
            top = d[key]
        
    return char




    