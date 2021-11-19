#attempt1:
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x ^= y
        c = 0
        while(x):
            c += x&1
            x >>= 1
        return c
        
