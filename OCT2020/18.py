#attempt3: 90% when k==n//2 it is a simple method -> simple method of largest profit
#if prices[i]>prices[i-1] = add to profit
#if k==len(prices)//2 -> help taken
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
        
#attempt2: at the most n//2 transactions can take place
#so k=min(k,n//2)
#TLE -> 210/212
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        k=min(len(prices)//2,k)
        if not(prices) or not(k):
            return 0
        buy=[-float('inf') for i in range(k)]
        sell=[-float('inf') for i in range(k)]
        for j in prices:
            buy[0]=max(buy[0],-j)
            sell[0]=max(sell[0],buy[0]+j)
            for i in range(1,k):
                buy[i]=max(buy[i],sell[i-1]-j)
                sell[i]=max(sell[i],buy[i]+j)
        return max(max(sell),0)
"""      

#attempt1: TLE 210/212 initially amount is 0
#you first buy amount is reduced, sell amount is added
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not(prices) or not(k):#very important conditions
            return 0
        buy=[-float('inf') for i in range(k)]
        sell=[-float('inf') for i in range(k)]
        for j in prices:
            buy[0]=max(buy[0],-j)
            sell[0]=max(sell[0],buy[0]+j)
            #current transaction can be the 1st,2nd or the kth transaction
            for i in range(1,k): 1<=k<=10**9 => TLE
                buy[i]=max(buy[i],sell[i-1]-j)
                sell[i]=max(sell[i],buy[i]+j)
        return max(max(sell),0)
"""
