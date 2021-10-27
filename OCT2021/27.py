#attempt1: Bucket Sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        di = {0:0,1:0,2:0}
        for i in nums:
            di[i] += 1
        index=0
        for i in di:
            while(di[i]):
                nums[index] = i
                index += 1
                di[i] -= 1
        