
class Interval(object):
    
    def __init__(self,a,b):
        """
        :a: integer
        :b: integer
        """
        assert isinstance(a,int)
        assert isinstance(b,int)
        assert a < b
        self._a = a
        self._b = b
    
    def __repr__(self):
        """Prints interval"""
        return '[Interval({},{})]'.format(self._a,self._b)
    
    def __eq__(self,other):
        """Determines if two intervals are equal"""
        return self._a == other._a and self._b == other._b
    
    
    def __lt__(self,other):
        """Determines if one interval is strictly less than another"""
        return self._b < other._a
    
    def __gt__(self,other):
        """Determines if one interval is strictly greater than another"""
        return self._a > other._b
    
    def __ge__(self,other):
        """Determines if one interval is greater than or equal to another"""
        return self._a >= other._b
    
    def __le__(self,other):
        """Determines if one interval is  less than or equal to another"""
        return self._b <= other._a
    
    def __add__(self,other):
        """Adds two intervals"""
        if self.intersect(other):
            return '[Interval({},{})]'.format(min(self._a,other._a), max(self._b,other._b))
        
        else:
            return '[Interval({},{}), Interval({},{})]'.format(self._a,self._b, other._a, other._b)
    
    def intersect(self,other):
        """Determines if two intervals intersect each other used in __add__"""
        
        if self._a < other._a:
            if self._b > other._a:
                return True
        
        elif self._a == other._a:
            return True
        
        elif self._a > other._a:
            if other._b > self._a:
                return True
        
        else:
            return False

