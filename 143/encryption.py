import string
import re
import random


def encrypt_message(message,fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 
    
    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    
    assert len(re.findall('[%s]' %string.punctuation,message)) == 0
    assert len(re.findall('[%s]' %string.ascii_uppercase,message)) == 0
    
    assert isinstance(message,str) and len(message) > 0
    assert isinstance(fname,str)
    
    
    lines = []
    message_lst = message.split(' ')
    
    with open(fname) as f:
        for line in f:
            line = re.sub('[%s]' % string.punctuation,'',line).strip().lower()
            lines.append(line.split())
            
    codex = dict()
    
    for i in lines:
        for j in i:
            word = i.index(j) 
            line_numb = lines.index(i) 
            if j in codex.keys():
            
                codex[j].append((line_numb,word))
                
            else:
                codex[j] = [(line_numb,word)]
    
    
    encryption = []
    
    for word in message_lst:
        assert word in codex
        assert len(codex[word]) > 0, "Not enough keys for encryption"
        lst = codex[word]
        tup = random.choice(lst)
        encryption.append(tup)
        codex[word].remove(tup)
        
   
    return encryption



def decrypt_message(inlist,fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 
    
    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    
    assert isinstance(inlist,list) and len(inlist) > 0
    for i in inlist:
        assert isinstance(i,tuple) and len(i) == 2
        for j in i:
            assert isinstance(j,int)
    
    lines = []
    
    with open(fname) as f:
        for line in f:
            line = re.sub('[%s]' % string.punctuation,'',line).strip().lower()
            lines.append(line.split())
            
    decryption = []
    
    for tup in inlist:
        row = tup[0] 
        column = tup[1] 
        decryption.append(lines[row][column])
    
    s = " ".join(decryption)
    s = s.strip()
    
    return s

