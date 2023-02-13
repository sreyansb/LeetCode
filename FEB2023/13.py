#attempt1:
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        totalNumber = high-low+1
        if totalNumber%2 == 0:
            return totalNumber//2
        else:
            return totalNumber//2+high%2
            
