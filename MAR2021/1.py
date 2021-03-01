#attempt1:
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)//2
        allc=set(candyType)
        if len(allc)>=n:
            return n
        return len(allc)
