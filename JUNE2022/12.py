#attempt2:
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxsum = 0
        sums = []
        prevsum = 0
        for i in nums:
            prevsum += i
            sums.append(prevsum)
        start_index = -1
        start_value = 0
        di = {}
        for end_index in range(len(nums)):
            if nums[end_index] in di and di[nums[end_index]] >= start_index:
                start_index = di[nums[end_index]]
            maxsum = max(maxsum,sums[end_index]-(0 if start_index==-1 else sums[start_index]))
            di[nums[end_index]] = end_index
            #print(maxsum,start_index)
        return maxsum

#attempt1:
'''
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxsum = 0
        di = {}
        currentsum = 0
        for index in range(len(nums)):
            ele = nums[index]
            if ele in di:
                currentsum -= di[ele]
            currentsum += ele
            di[ele] = currentsum
            maxsum = max(maxsum,currentsum)
        return maxsum
'''
