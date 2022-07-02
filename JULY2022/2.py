#attempt1:
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        maxdifferencehori = -float('inf')
        maxdifferencevert = -float('inf')
        for i in range(1,len(horizontalCuts)):
            maxdifferencehori = max(maxdifferencehori,horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1,len(verticalCuts)):
            maxdifferencevert = max(maxdifferencevert,verticalCuts[i]-verticalCuts[i-1])
        #print(horizontalCuts,verticalCuts,maxdifferencehori,maxdifferencevert)
        return (maxdifferencehori*maxdifferencevert)%(1000000007)

