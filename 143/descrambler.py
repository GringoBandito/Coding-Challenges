import itertools as it
import urllib

url = "https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt"
file = urllib.request.urlopen(url)
d = {}


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


for line in file:
    decoded_line = str(line.decode("utf-8"))
    decoded_line = decoded_line.strip()
    
    if toword(sorted(decoded_line)) not in d.keys():
        d[toword(sorted(decoded_line))] = [decoded_line]
    
    else:
        d[toword(sorted(decoded_line))].append(decoded_line)
        
    

w = 'googold'


x = it.combinations(w,3)
y = [''.join(i) for i in x]
y = set(y)
y = list(y)
y = [toword(sorted(i)) for i in y ]
lst = [i for i in y if i in d.keys()]


xx = it.combinations(w,2)
xxx = it.combinations(w,2)
yy = [''.join(i) for i in xx]
yy = set(yy)
yy = list(yy)
yy = [toword(sorted(i)) for i in yy]
lst2 = [i for i in yy if i in d.keys()]

yyy = [''.join(i) for i in xxx]
yyy = set(yyy)
yyy = list(yyy)
yyy = [toword(sorted(i)) for i in yyy]
lst3 = [i for i in yyy if i in d.keys()]

trial = []


for i in lst:
    for j in lst2:
        for k in lst3:
            test = it.product(d[i],d[j],d[k])
            
            for prod in test:
                if sorted(''.join(prod)) == sorted(w):
                    trial.append(' '.join(prod))
 
            
            
trial = set(trial)
trial = list(trial)             



lst_test = [lst,lst2,lst3]
all_word = it.product(*lst_test)
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
for i in paragraph:
    " ".join(i)
#all_word = list(all_word)
