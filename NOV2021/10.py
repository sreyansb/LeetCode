#attempt1:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buys = [0 for i in range(n)]
        sells = [0 for i in range(n)]
        buys[0] = -prices[0]
        sells[0] = 0
        for i in range(1,n):
            buys[i] = max(buys[i-1],sells[i-1]-prices[i])
            sells[i] = max(sells[i-1],buys[i]+prices[i])
        return max(0,max(sells))
