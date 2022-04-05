#attempt1: TOOK HINT
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        maxarea = -float('inf')
        while(left<right):
            width = right-left+1-1
            heightmin = min(height[left],height[right])
            maxarea = max(maxarea,width*heightmin)
            if height[left]>height[right]:
                right -= 1
            else:
                left += 1
        return maxarea

