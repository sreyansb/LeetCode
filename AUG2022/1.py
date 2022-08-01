#attempt2:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(None)
        def findpaths(currow,curcol):
            if currow>=m or curcol>=n:
                return 0
            if currow == m-1 and curcol == n-1:
                return 1
            return findpaths(currow+1,curcol)+findpaths(currow,curcol+1)
        
        return findpaths(0,0)
        

#attempt1:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(None)
        def findpaths(currow,curcol):
            if not(0<=currow<m) or not(0<=curcol<n):
                return 0
            if currow == m-1 and curcol == n-1:
                return 1
            return findpaths(currow+1,curcol)+findpaths(currow,curcol+1)
        
        return findpaths(0,0)
        
