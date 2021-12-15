import re 
import string


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
    
    assert isinstance(message, str)
    assert isinstance(fname, str)
    
    answer = []
    found = False
    
    
    for word in message.split():
        assert word.islower()
        for i in range(len(word)):
            assert word[i] in 'abcdedfghijklmnopqrstuvwxyz'
            
        count = 0
        found = False
        
        with open(fname, 'r') as f:
            while not found:
                line = f.readline()
                if not line:
                    break
                
                count += 1
                wordcount = 0
                
                for j in re.sub('['+string.punctuation+']', '', line).split():
                    wordcount += 1
                    j = j.lower()
                    
                    if word == j:
                        temp = (count, wordcount)
                        
                        if temp not in answer:
                            answer.append(temp)
                            found = True
                            break
                        
        assert found == True, 'Word is not in file'
        f.close()
        
        
    return answer


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
    
    answer = ''
    
    for encoding in inlist:
        assert isinstance(encoding, tuple)
        assert len(encoding) == 2
        assert isinstance(encoding[0], int)
        assert isinstance(encoding[1], int)
        assert encoding[0] >= 1
        assert encoding[1] >= 1
        
        count = 0
        wordcount = 0
        found = False
        
        
        with open(fname, 'r') as f:
            while not found:
                count += 1
                line = f.readline()
                if not line:
                    break
                
                if count == encoding[0]:
                    for word in re.sub('['+string.punctuation+']', '', line).split():
                        wordcount += 1
                        
                        if wordcount == encoding[1]:
                            word = word.lower()
                            answer += word
                            answer += " "
                            found = True
                            
        f.close()
        
        
    return answer[:-1]

