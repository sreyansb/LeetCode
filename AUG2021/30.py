#attempt1: Looks difficult
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        xmin=m
        ymin=n
        for xx,xy in ops:
            xmin=min(xmin,xx)
            ymin=min(ymin,xy)
        return xmin*ymin