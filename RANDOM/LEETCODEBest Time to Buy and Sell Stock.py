from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        mintillnow=inf
        for i in range(len(prices)):
            if prices[i]<=mintillnow:
                mintillnow=prices[i]
            else:
                maxi=max(maxi,prices[i]-mintillnow)
        return maxi
        
