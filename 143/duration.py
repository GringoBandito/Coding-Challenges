from time import sleep 
import random
from datetime import datetime
import itertools as it
from types import GeneratorType


def producer():
     'produce timestamps'
     starttime = datetime.now()
     while True:
         sleep(random.uniform(0,0.2))
         yield datetime.now()-starttime
         

p = producer()

def tracker(p, limit=2):
    '''runs input generator p limit number of times of odd seconds'''
    assert isinstance(p,GeneratorType)
    assert isinstance(limit, int) and limit > 0
    
    count = 0
    while True:
        val = next(p).seconds % 2
        if val % 2:
            count += 1
        
        rval = yield count
        if rval is not None:
            assert isinstance(rval,int) and rval > 0
            limit = rval
        
        if count >= limit:
            break
        



t = tracker(p,5)


print(list(t))
    


