from math import gcd
class Rational():
    
    def __init__(self,p,q):
        """Class of rational numbers"""
        assert isinstance(p,int)
        assert isinstance(q,int) and q != 0
        
        
        self.p = p
        self.q = q
        
        
    def __repr__(self):
        g = gcd(self.p,self.q)
        if self.q/g == 1:
            return str(int(self.p/g))  
       
        else:
            return str(int(self.p/g)) + '/' + str(int(self.q/g)) 

    def __truediv__(self,other):
        return Rational(self.p,other*self.q)
    
    def __rtruediv__(self,other):
        return Rational(self.q * other, self.p)
    
    def __neg__(self):
        return Rational(-self.p,self.q)
    
    def __int__(self):
        return int(self.p/self.q)
    
    def __float__(self):
        return float(self.p/self.q)
    
    def __add__(self,other):
        return Rational(self.p * other.q + other.p * self.q,self.q * other.q)
    
    def __sub__(self,other):
        return Rational(self.p * other.q - other.p * self.q,self.q * other.q)
    
    def __mul__(self,other):
        if isinstance(other,Rational):
            return Rational(self.p * other.p, self.q * other.q)
        
        elif isinstance(other,int) or isinstance(other,float):
            return Rational(self.p * other, self.q)
    
    def __eq__(self,other):
        g1 = gcd(self.p,self.q)
        g2 = gcd(other.p, other.q)
        return self.p/g1 == other.p/g2 and self.q/g1 == other.q/g2
        
        
        
    def __gt__(self,other):
        if self.p * other.q > self.q * other.p:
            return True
        
        else:
            return False

    def __lt__(self,other):
        if self.p * other.q < self.q * other.p:
            return True
        
        else:
            return False
        
    def __ge__(self,other):
        if self.p * other.q >= self.q * other.p:
            return True
        
        else:
            return False
        
    def __le__(self,other):
        if self.p * other.q <= self.q * other.p:
            return True
        
        else:
            return False
        
