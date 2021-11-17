#attempt1:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def findpaths(r,c):
            if not(1<=r<=m and 1<=c<=n):
                return 0
            if (r==m and c==n):
                return 1
            return findpaths(r+1,c)+findpaths(r,c+1)
        return findpaths(1,1)
                
            
        
