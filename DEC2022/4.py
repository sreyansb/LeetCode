#attempt1:
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        average_from_left = [0]*n
        average_from_right = [0]*n
        left_sum = 0
        for index in range(n):
            left_sum += nums[index]
            average_from_left[index] = left_sum//(index+1)
        right_sum = 0
        min_index = -1
        min_ans = float('inf')
        for index in range(n-1,-1,-1):
            try:
                average_from_right[index] = right_sum//(n-index-1)
            except:
                average_from_right[index] = 0
            diff_here = abs(average_from_left[index] - average_from_right[index])
            if diff_here <= min_ans:
                min_ans = diff_here
                min_index = index
            right_sum += nums[index]
        return min_index
        
        
