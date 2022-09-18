#attempt1:
class Solution:
    def trap(self, heights: List[int]) -> int:
        ans = 0
        max_on_left = [heights[0]]*len(heights)
        for index in range(1,len(heights)):
            max_on_left[index] = max(max_on_left[index-1],heights[index])
        max_till_now = heights[-1]
        for index in range(len(heights)-2,0,-1):
            height = heights[index]
            max_till_now = max(max_till_now,height)
            ans += max(0,min(max_till_now,max_on_left[index])-height)
        return ans
        
