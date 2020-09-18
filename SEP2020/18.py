#attemp2:80% and 88%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not(prices):
            return 0
        mini=float('inf')
        maxp=0
        for i in prices:
            if i-mini:
                maxp=max(maxp,i-mini)
            mini=min(mini,i)
        return (maxp)
        

#attempt1 : 80% and 20%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not(prices):#very important condition
            return 0
        mini=max(prices)
        maxp=0
        for i in prices:
            if i-mini:
                maxp=max(maxp,i-mini)
            mini=min(mini,i)
        return (maxp)
        
