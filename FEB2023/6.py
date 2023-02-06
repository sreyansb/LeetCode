#attempt1:
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        x = nums[:n//2]
        y = nums[n//2:]
        xindex,yindex = 0,0
        for index in range(n):
            if index % 2:
                nums[index] = y[yindex]
                yindex += 1
            else:
                nums[index] = x[xindex]
                xindex += 1
        return nums
