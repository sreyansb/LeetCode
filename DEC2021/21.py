#attempt2:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and n&(n-1) == 0
        
#attempt1: WA Didn't take care of 0
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n&(n-1) == 0
'''
