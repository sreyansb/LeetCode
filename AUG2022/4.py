#attempt2:
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if p == q:
            return 1
        if q == 1:
            return 1 if p%2 else 2
        while(p%2==0 and q%2==0):
            p //= 2
            q //= 2
        if p%2:
            return q%2
        if p&(p-1) == 0:
            return 2
        if q&(q-1) == 0 and q != 2:
            return 0
        return 1 if q%2==0 else 2

#attempt1: WA because p and q need to be divided until ether is odd
'''
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if p == q:
            return 1
        if q == 1:
            return 1 if p%2 else 2
        if p%2:
            return q%2
        if p&(p-1) == 0:
            return 2
        if q&(q-1) == 0 and q != 2:
            return 0
        return 1 if q%2==0 else 2
'''
