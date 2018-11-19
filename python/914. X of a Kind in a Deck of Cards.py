class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # 1. 找最大公约数 Greatest Common Divisor
        from collections import Counter
        
        count = Counter(deck).values()
        
        from fractions import gcd   # gcd is a function finding the greatest common divisor of a,b     gcd(a,b)
        from functools import reduce   # reduce(func, iterable)    is to apply the function func into a iterable object
        group = reduce(gcd, count)
        
        if group >=2:
            return True
        else:
            return False
        
