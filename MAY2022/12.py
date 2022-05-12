#attempt1:
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def reverse(left,right):
            while(left<right):
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        nums.sort()
        n = len(nums)
        final = {tuple(nums)}
        
        while(True):
            rightmost = -1
            for i in range(n-2,-1,-1):
                if nums[i]<nums[i+1]:
                    rightmost = i
                    break
            if rightmost == -1:
                break
            for i in range(n-1,rightmost,-1):
                if nums[i]>nums[rightmost]:
                    nums[i],nums[rightmost] = nums[rightmost],nums[i]
                    break
            reverse(rightmost+1,n-1)
            final.add(tuple(nums))
        return final
        
