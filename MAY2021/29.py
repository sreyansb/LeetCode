class Solution:
    def totalNQueens(self, n: int) -> int:
        ans=[0]
        def recurse(leng,dp):
            if leng==n:
                ans[0]+=1
                return
            for j in range(n):
                if dp[leng][j]:
                    continue
                dp[leng][j]=1
                for i in range(n):
                    dp[leng][i]+=1
                    dp[i][j]+=1
                for row in range(n):
                    for col in range(n):
                        if row-col==leng-j:
                            dp[row][col]+=1
                        if row+col==leng+j:
                            dp[row][col]+=1
                recurse(leng+1,dp)
                dp[leng][j]-=1
                for i in range(n):
                    dp[leng][i]-=1
                    dp[i][j]-=1
                for row in range(n):
                    for col in range(n):
                        if row-col==leng-j:
                            dp[row][col]-=1
                        if row+col==leng+j:
                            dp[row][col]-=1
        dp=[[0 for i in range(n)]for j in range(n)]
        recurse(0,dp)
        return ans[0]