import itertools as it


def toword(word):
    final = ''
    for i in word:
        final = final + i
    
    return final

def list_to_word(lst):
    word = ''
    for i in lst:
        word += i
    
    return word


def descrambler(w,k):
    """Input: scrambled set of words str(k) 
              tuple of the length of possible words 
        
        Return: Possible sequence of valid words"""
        
    assert isinstance(w,str) and len(w) > 0
    assert isinstance(k,tuple)
    assert sum(k) == len(w)
    for i in k:
        assert isinstance(i,int) and i > 0
    
    path = "/tmp/google-10000-english-no-swears.txt"

    d = {}
    with open(path, 'r') as f:
        for line in f:
            decoded_line = str(line)
            decoded_line = decoded_line.strip()
    
            if toword(sorted(decoded_line)) not in d.keys():
                d[toword(sorted(decoded_line))] = [decoded_line]
    
            else:
                d[toword(sorted(decoded_line))].append(decoded_line)
    
    lst = []
    
    for i in k:
        x = it.combinations(w,i)
        y = [''.join(i) for i in x]
        y = set(y)
        y = list(y)
        y = [toword(sorted(i)) for i in y ]
        lst2 = [i for i in y if i in d.keys()]
        lst.append(lst2)

    all_word = it.product(*lst)
    all_word = list(all_word)
    all_word = [' '.join(i) for i in all_word if sorted(''.join(i)) == sorted(w)]
    all_word = set(all_word)
    all_word = list(all_word)
    
    sentence = []
    
    for i in all_word:
        test = i.split(" ")
        for j in test:
            sentence.append(d[j])
    
    paragraph = it.product(*sentence)
    paragraph = set(paragraph)
    paragraph = list(paragraph)
    
    if len(paragraph) == 0:
        yield []
    
    while len(paragraph) > 0:
        option = " ".join(paragraph[0])
        del paragraph[0]
        yield option
    
    
