#attempt2:
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum = 0
        pre_seen_sums = {}
        for index,num in enumerate([0] + nums):
            pre_sum += num
            #print(pre_sum%k,pre_seen_sums)
            if pre_sum%k in pre_seen_sums and index - pre_seen_sums[pre_sum%k] > 1:
                return True
            if pre_sum%k not in pre_seen_sums:
                pre_seen_sums[pre_sum%k] = index
        return False

#attempt1:
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        pre_compute_sum = [0]*(n+1)
        for index in range(1,n+1):
            pre_compute_sum[index] = pre_compute_sum[index-1] + nums[index-1]
        pre_seen_sums = {}
        for index,pre_sum in enumerate(pre_compute_sum):
            #print(pre_sum%k,pre_seen_sums)
            if pre_sum%k in pre_seen_sums and index - pre_seen_sums[pre_sum%k] > 1:
                return True
            if pre_sum%k not in pre_seen_sums:
                pre_seen_sums[pre_sum%k] = index
        return False
        
