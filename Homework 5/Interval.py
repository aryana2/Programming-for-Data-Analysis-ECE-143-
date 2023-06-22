class Interval(object):
    def __init__(self,a,b):
        """
        :a: integer
        :b: integer
        """
        assert a<b
        assert isinstance(a,int)
        assert isinstance(b,int)
        assert b != 0
        self._a = a
        self._b = b
        
    def __repr__(self):
        """
        :self: Interval
        """
        return "Interval({},{})".format(self._a,self._b)

    def __eq__(self,other):
        """
        :self: Interval
        :other: Interval
        """
        return self._a==other._a and self._b==other._b

    def __lt__(self,other):
        """
        :self: Interval
        :other: Interval
        """
        print()
        return self._b<other._b

    def __gt__(self,other):
        """
        :self: Interval
        :other: Interval
        """
        return self._b>other._b

    def __ge__(self,other):
        """
        :self: Interval
        :other: Interval
        """
        return self._b>=other._b

    def __le__(self,other):
        """
        :self: Interval
        :other: Interval
        """
        return self._b<=other._b

    def __add__(self,other): 
        """
        :self: Interval
        :other: Interval
        """
        if self.intersected(other):
            return Interval(min(self._a,other._a), max(self._b,other._b))
        else:
            return [Interval(self._a, self._b), Interval(other._a, other._b)]
        
    
    def intersected(self,other):
        """
        Find whether self intersects with other
        :self: Interval
        :other: Interval
        """
        if other._a<=self._a:
            if other._b>self._a:
                return True
            else:
                return False
        elif self._a<other._a and other._a<self._b:
            return True
        else:
            return False