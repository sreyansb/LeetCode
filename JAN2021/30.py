#attempt1: TOOK HELP
from heapq import heapify,heappop,heappush
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums=list(set([-i*2 if i&1 else -i for i in nums]))
        heapify(nums)
        maxi,mini=-nums[0],-max(nums)
        diff=maxi-mini
        while(-nums[0]%2==0):
            m=heappop(nums)//2
            heappush(nums,m)
            maxi,mini=-nums[0],min(mini,-m)
            diff=min(diff,maxi-mini)
        return diff
