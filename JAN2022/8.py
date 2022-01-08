#attempt2: 1220ms
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ans = [0]
        
        rlim = len(grid)
        clim = len(grid[0])
        
        @lru_cache(None)
        def recurse(rob1r,rob1c,rob2r,rob2c):
            if rob1r>=rlim and rob2r>=rlim:
                return 0
            curans = grid[rob1r][rob1c] + grid[rob2r][rob2c] - (grid[rob1r][rob1c] if (rob1r,rob1c)==(rob2r,rob2c) else 0)
            maxans = 0
            for new1r,new1c in [(rob1r+1,rob1c-1),(rob1r+1,rob1c+1),(rob1r+1,rob1c)]:
                if (0<=new1c<clim):
                    for new2r,new2c in [(rob2r+1,rob2c-1),(rob2r+1,rob2c+1),(rob2r+1,rob2c)]:
                        if (0<=new2c<clim):
                            maxans = max(maxans,recurse(new1r,new1c,new2r,new2c))
            curans += maxans
            ans[0] = max(ans[0],curans)
            return curans
        
        recurse(0,0,0,clim-1)
        return ans[0]
                        
#attempt1: 1870ms
'''
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ans = [0]
        
        rlim = len(grid)
        clim = len(grid[0])
        
        @lru_cache(None)
        def recurse(rob1r,rob1c,rob2r,rob2c):
            if rob1r>=rlim and rob2r>=rlim:
                return 0
            curans = grid[rob1r][rob1c] + grid[rob2r][rob2c] - (grid[rob1r][rob1c] if (rob1r,rob1c)==(rob2r,rob2c) else 0)
            maxans = 0
            for new1r,new1c in [(rob1r+1,rob1c-1),(rob1r+1,rob1c+1),(rob1r+1,rob1c)]:
                if (0<=new1c<clim):
                    for new2r,new2c in [(rob2r+1,rob2c-1),(rob2r+1,rob2c+1),(rob2r+1,rob2c)]:
                        if (0<=new2c<clim):
                            maxans = max(maxans,recurse(new1r,new1c,new2r,new2c))
            ans[0] = max(ans[0],curans+maxans)
            return curans+maxans
        
        recurse(0,0,0,clim-1)
        return ans[0]
'''
