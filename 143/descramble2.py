import itertools as it

import numpy as np
import itertools as it
import urllib

url = "https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt"
file = urllib.request.urlopen(url)
d = {}

for line in file:
    decoded_line = str(line.decode("utf-8"))
    decoded_line = decoded_line.strip()
    d[decoded_line] = 1


def descrambler(w,k):
    """Input: scrambled set of words str(k) 
              tuple of the length of possible words 
        
        Return: Possible sequence of valid words"""
        
    assert isinstance(w,str) and len(w) > 0
    assert isinstance(k,tuple)
    assert sum(k) == len(w)
    
    lst = []
    
    for i in k:
        x = it.permutations(w,i)
        y = [''.join(i) for i in x]
        y = set(sorted(y))
        y = list(y)
        lst2 = [i for i in y if i in d.keys()]
        lst.append(lst2)

    all_word = it.product(*lst)
    all_word = list(all_word)
    all_word = [' '.join(i) for i in all_word if check_perm(''.join(i),w)]
   
    
    while len(all_word) > 0:
        option = all_word[0]
        del all_word[0]
        yield option

w = 'qeodwnsciseuesincereins'
test_case = list(descrambler(w,(4,7,12)))