#attempt1: Had no clue->took HELP
#this code explanation: have two robots decided by column names
#both robots are in the same row but different columns
#if both in same location add only once
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        mins=-float('inf')
        dp={}
        def recurse(row,col1,col2):#both robot1 and robot2 need to be in same row
            if row>=rows:
                return 0
            if col1<0 or col1>=cols or col2<0 or col2>=cols:
                return 0
            ans=mins
            curs=grid[row][col1]+grid[row][col2]
            if col1==col2:
                curs-=grid[row][col1]
            if (row,col1,col2) in dp:
                return dp[(row,col1,col2)]
            ans=max(ans,curs+recurse(row+1,col1,col2))
            ans=max(ans,curs+recurse(row+1,col1,col2+1))
            ans=max(ans,curs+recurse(row+1,col1,col2-1))
            ans=max(ans,curs+recurse(row+1,col1+1,col2))
            ans=max(ans,curs+recurse(row+1,col1+1,col2+1))
            ans=max(ans,curs+recurse(row+1,col1+1,col2-1))
            ans=max(ans,curs+recurse(row+1,col1-1,col2))
            ans=max(ans,curs+recurse(row+1,col1-1,col2+1))
            ans=max(ans,curs+recurse(row+1,col1-1,col2-1))
            dp[(row,col1,col2)]=ans
            return ans
        return recurse(0,0,cols-1)
