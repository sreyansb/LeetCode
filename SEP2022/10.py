#attempt1:
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not(n) or not(k):
            return 0
        if k>=n/2:
            totalProfit = 0
            for index in range(1,len(prices)):
                if prices[index] > prices[index-1]:
                    totalProfit += prices[index] - prices[index-1]
            return totalProfit
        buys = [-float('inf') for i in range(k)]
        sells = [-float('inf') for i in range(k)]
        for price in prices:
            buys[0] = max(buys[0],-price)
            sells[0] = max(sells[0],buys[0]+price)
            for curk in range(1,k):
                buys[curk] = max(buys[curk],sells[curk-1]-price)
                sells[curk] = max(sells[curk],buys[curk]+price)
        return max(0,max(sells))
        
