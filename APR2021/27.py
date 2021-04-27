#attempt3:
from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        if n<0:
            return False
        while(n>1):
            if n%3!=0:
                return False
            n//=3
        return True
            
        

#attempt2: AC committing same mistake
'''
from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        z=log(n)/log(3)
        return abs(z-int(z))<=0.00000001 or abs(z-int(z)-1)<=0.0000000001
        
'''

#attempt1:WA committing same mistake
'''
from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        z=log(n)/log(3)
        return z==int(z)
        
'''
