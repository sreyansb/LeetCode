#attempt1:
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        increasing  = [1 for i in range(n)]
        decreasing = [1 for i in range(n)]
        for head_index in range(n-2,-1,-1):
            for other_index in range(head_index+1,n):
                if nums[head_index] < nums[other_index]:
                    decreasing[head_index] = max(decreasing[head_index],increasing[other_index]+1)
                elif nums[head_index] > nums[other_index]:
                    increasing[head_index] = max(increasing[head_index],decreasing[other_index]+1)
        return max(max(increasing),max(decreasing))
                
            
