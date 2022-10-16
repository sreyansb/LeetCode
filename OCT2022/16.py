#attempt1:
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        #dLeft-1 = n-newIndex
        #newIndex = n-dLeft+1
        
        @lru_cache(None)        
        def findAns(curIndex,dLeft):
            if curIndex >= n:
                return 0
            if dLeft <= 0:
                return float('inf')
            minAns = float('inf')
            maxForSeries = -float('inf')
            for nextIndex in range(curIndex,n-dLeft+1):
                maxForSeries = max(maxForSeries,jobDifficulty[nextIndex])
                minAns = min(minAns,maxForSeries+findAns(nextIndex+1,dLeft-1))
            return minAns
        
        return findAns(0,d)
                
