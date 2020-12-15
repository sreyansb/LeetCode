#attempt1:
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not(nums):
            return []
        left=0
        right=len(nums)-1
        intofill=right
        ans=[0]*(right+1)
        while(left<=right):
            if abs(nums[left])<abs(nums[right]):
                ans[intofill]=nums[right]*nums[right]
                right-=1
                intofill-=1
            else:
                ans[intofill]=nums[left]*nums[left]
                left+=1
                intofill-=1
        return ans
                
