#attempt1: very nice problem
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dpt={}
        def dfs(currow,curcol,moves):
            if (currow<0 or curcol<0 or currow>=m or curcol>=n) and moves>=0:
                return 1
            if moves<=0:
                return 0
            if (currow,curcol,moves) in dpt:
                return dpt[(currow,curcol,moves)]
            ans=0
            for r,c in [(0,1),(0,-1),(1,0),(-1,0)]:
                ans+=dfs(currow+r,curcol+c,moves-1)
            dpt[(currow,curcol,moves)]=ans%(1000000007)
            return dpt[(currow,curcol,moves)]
        return dfs(startRow,startColumn,maxMove)
                