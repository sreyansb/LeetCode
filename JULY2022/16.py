#attempt1:
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 1000000007
        
        @lru_cache(None)
        def findans(row,col,maxMove):
            if not(0<=row<m) or not(0<=col<n):
                return 1
            if maxMove == 0:
                return 0
            return (findans(row-1,col,maxMove-1) + findans(row+1,col,maxMove-1) + findans(row,col-1,maxMove-1) + findans(row,col+1,maxMove-1))%mod
        
        return findans(startRow,startColumn,maxMove)
    
            
        
