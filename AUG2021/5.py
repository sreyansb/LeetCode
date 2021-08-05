#attempt1: You only need to do it for current and maximize the value for this
from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        @lru_cache(None)
        def recurse(start,end,s):
            if start>end:
                return s
            return max(piles[start]-recurse(start+1,end,s-piles[start]),piles[end]-recurse(start,end-1,s-piles[end]))
        return recurse(0,len(piles)-1,sum(piles))>0
            
        