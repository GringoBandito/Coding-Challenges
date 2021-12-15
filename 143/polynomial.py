from collections import OrderedDict

class Polynomial():
    
    def __init__(self,d):
        
        self.d = OrderedDict(sorted(d.items(), key=lambda x: x[0]))
        for key,value in self.d.items():
            assert isinstance(value,int)
        
    def __repr__(self):
        
        s = ''
        
        for key,value in self.d.items():
            if key == 0 and value != 0:
                s += str(value)
                
            elif key == 1 and value != 0 :
                s += ' + ' + str(value) + ' x'
                
            else:
                if value != 0:
                    s += ' + ' + str(value) + ' x^(' +  str(key) +')'
                
        return s
    
    def __mul__(self,other):
        d2 = dict()
        if isinstance(other,int):
            
            for key in self.d:
                d2[key] = self.d[key] * other
            
            return Polynomial(d2)
        
        if isinstance(other,Polynomial):
            for key,value in self.d.items():
                for k,v in other.d.items():
                    power = k + key
                    coeff = value * v
                    
                    if power in d2.keys():
                        d2[power] += coeff
                        
                    else:
                        d2[power] = coeff
                        
            return Polynomial(d2)
    
    def __rmul__(self,other):
        if isinstance(other,int):
            d2 = dict()
            for key in self.d:
                d2[key] = self.d[key] * other
            
            return Polynomial(d2)
            
        
    def __add__(self,other):
        if isinstance(self,Polynomial) and isinstance(other,Polynomial):
            d2 = dict()
            for key, value in other.d.items():
                if key in self.d.keys():
                    d2[key] = self.d[key] + value
                
                else:
                    d2[key] = value
            
            for key,value in self.d.items():
                if key not in other.d.keys():
                    d2[key] = value
            
            return Polynomial(d2)
    
        elif isinstance(self,Polynomial) and isinstance(other,int):
            d2 = self.d
            d2[0] += other
                
            return Polynomial(d2)
        
    def __radd__(self,other):
         if isinstance(self,Polynomial) and isinstance(other,int):
            d2 = self.d
            d2[0] += other
    
            return Polynomial(self.d)
        
    def __sub__(self,other):
        d2 = self.d
        if isinstance(self,Polynomial) and isinstance(other,Polynomial):
            for key, value in other.d.items():
                if key in self.d.keys():
                    d2[key] -= value
                
                else:
                    d2[key] = -value
            
            return Polynomial(d2)
    
        elif isinstance(self,Polynomial) and isinstance(other,int):
            d2[0] -= other
                
            return Polynomial(d2)
    
    
    def __rsub__(self,other):
        d2 = self.d
        if isinstance(self,Polynomial) and isinstance(other,int):
            d2[0] =  -d2[0] + other 
            
            for key,value in d2.items():
                d2[key] = -d2[key]
    
            return Polynomial(d2)
        
    
    def __eq__(self,other):
        
        if isinstance(other,Polynomial):
            if self.d == other.d:
                return True
        
            else:
                return False
            
        elif other == 0:
            for key in self.d:
                if self.d[key] != 0:
                    return False
                
            return True
        
    def __truediv__(self,other):
        
        if isinstance(other,Polynomial):
            assert not(other == 0)
            q = Polynomial({0:0})
            r = Polynomial(self.d)
            degr = max(list(r.d.keys()))
            degd = max(list(other.d.keys()))
            d2 = dict()
            while not(r==0) and degr >= degd:
                deg = degr - degd
                num = r.d[degr]
                denom = other.d[degd]
                coeff = int(num/denom)
                d2[deg] = coeff
                t = Polynomial({deg:coeff})
                q = q + t
                
                term = t * other
                r = r - term
        
                if r == 0:
                    return Polynomial(d2)
                
                for key,value in r.d.items():
                    if value == 0:
                        del r.d[key]
                        
                degr = max(list(r.d.keys()))
        
        if r != 0:
            raise NotImplementedError 
        
        
        
        
    def subs(self,x):
        assert isinstance(x,int)
        count = 0
        for key,value in self.d.items():
            count += x**key * value
    
        return count



