#attempt1: Had no lcue. It is about finding a minimum until current element(leftmost
#occurence of that number) and then use that to find max difference
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        maxp = 0
        for i in prices:
            if i!=mini:
                mini = min(mini,i)
            maxp = max(maxp,i-mini)
        return maxp
        
        
