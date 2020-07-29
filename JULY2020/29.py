#took help, tried a lot, it was very difficult
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n<2:
            return 0
        elif n==2:
            return max(0,prices[1]-prices[0])
        else:
            dp=[[0 for i in range(2)] for j in range(n)]
            dp[0][1]=-prices[0]
            dp[1][0]=max(dp[0][1]+prices[1],dp[0][0])
            dp[1][1]=max(-prices[1],dp[0][1])
            for i in range(2,n):
                dp[i][1]=max(dp[i-1][1],dp[i-2][0]-prices[i])
                dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
            return dp[n-1][0]
        
