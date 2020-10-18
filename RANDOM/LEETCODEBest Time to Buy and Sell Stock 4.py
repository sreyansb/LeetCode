class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        k=min(len(prices)//2,k)
        if not(prices) or not(k):
            return 0
        if k==len(prices)//2:
            profit=0
            for i in range(1,len(prices)):
                if prices[i]>prices[i-1]:
                    profit+=prices[i]-prices[i-1]
            return profit
        buy=[-float('inf') for i in range(k)]
        sell=[-float('inf') for i in range(k)]
        for j in prices:
            buy[0]=max(buy[0],-j)
            sell[0]=max(sell[0],buy[0]+j)
            for i in range(1,k):
                buy[i]=max(buy[i],sell[i-1]-j)
                sell[i]=max(sell[i],buy[i]+j)
        return max(max(sell),0)
        
