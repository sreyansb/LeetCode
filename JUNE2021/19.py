#attempt1: TOOK HELP
#  It is quite a problem, very difficult to think of
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        #for a number n only (n*(n-1))//2 swaps are possible at max
        #let's consider a DP with DP[i][j] implies with i elements and j inversions
        #we need to find DP[n][k]
        if n==0:
            return 0
        if k==0:
            return 1
        dp=[[0 for i in range(k+1)] for j in range(n+1)]
        for i in range(1,n+1):
            dp[i][0]=1
            for j in range(1,k+1):
                if j-i>=0:
                    dp[i][j]=dp[i-1][j]-dp[i-1][j-i]
                else:
                    dp[i][j]=dp[i-1][j]
                dp[i][j]+=dp[i][j-1]
        #print(dp)
        return (dp[n][k]-dp[n][k-1])%(1000000007)
                
        