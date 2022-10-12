#attempt1:
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for index in range(n-3,-1,-1):
            a,b,c = nums[index],nums[index+1],nums[index+2]
            if a+b > c and b+c > a and a+c > b:
                return a+b+c
        return 0
        
