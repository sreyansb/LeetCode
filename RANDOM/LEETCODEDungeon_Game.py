#attempt2: TOOK HELP :It is a bottom Up approach.
#according to what I understood the state of DP at DP[r][c]: is the value
#needed to cross that dungeon cell and enter into the adjacent cells
# therefore the dp value is max(1,-dungeon[r][c]+min(dp[r+1][c],dp[r][c+1]))
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n=len(dungeon),len(dungeon[0])
        dp=[[0 for i in range(n)]for j in range(m)]
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if row==m-1 and col==n-1:
                    dp[row][col]=max(1,-dungeon[row][col]+1)
                elif row==m-1:
                    dp[row][col]=max(1,-dungeon[row][col]+dp[row][col+1])
                elif col==n-1:
                    dp[row][col]=max(1,-dungeon[row][col]+dp[row+1][col])
                else:
                    dp[row][col]=max(1,-dungeon[row][col]+min(dp[row+1][col],dp[row][col+1]))
        return dp[0][0]

#attempt1: The thing is we need to find the smallest value in the path
#of all the paths possible find the max smallest number and 
#answer is max(1,-(largest least)+1)
'''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n=len(dungeon),len(dungeon[0])
        ans=[-float('inf')]
        def find(r,c,cursum,mintillhere):
            if not(0<=r<m) or not(0<=c<n):
                return -float('inf')
            if r==m-1 and c==n-1:
                ans[0]=max(ans[0],min(cursum+dungeon[r][c],mintillhere))
                return
            find(r+1,c,cursum+dungeon[r][c],min(mintillhere,cursum+dungeon[r][c]))
            find(r,c+1,cursum+dungeon[r][c],min(mintillhere,cursum+dungeon[r][c]))
        find(0,0,0,float('inf'))
        return max(0,-ans[0])+1
'''