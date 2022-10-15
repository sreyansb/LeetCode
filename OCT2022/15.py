#attempt1: TOOK HELP : COPIED
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        
        @lru_cache(None)
        def findAns(curK,curIndex,pastIndex,countTillNow):
            if curK < 0:
                return float('inf')
            if curIndex >= n:
                return 0
            if pastIndex > -1 and s[curIndex] == s[pastIndex]:
                return (countTillNow in [1,9,99]) + findAns(curK,curIndex+1,curIndex,countTillNow+1)
            return min(1 + findAns(curK,curIndex+1,curIndex,1),findAns(curK-1,curIndex+1,pastIndex,countTillNow))
        
        return findAns(k,0,-1,0)
        
            
