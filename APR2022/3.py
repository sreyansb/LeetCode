#attempt1:
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if nums == sorted(nums,reverse=True):
            nums.sort()
            return
        pos = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                pos = i
                break
        post = -1
        for i in range(len(nums)-1,pos,-1):
            if nums[i] > nums[pos]:
                post = i
                break
        nums[post],nums[pos] = nums[pos],nums[post]
        low = pos+1
        end = len(nums)-1
        while(low<end):
            nums[low],nums[end] = nums[end],nums[low]
            low += 1
            end -= 1
        return
