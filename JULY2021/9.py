#aattempt2:
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        ans=[]
        for i in range(n):
            pos=bisect_left(ans,nums[i])
            if pos==len(ans):
                ans.append(i)
            ans[pos]=nums[i]
        return len(ans)

#attempt1: O(n2)
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        arr=[1 for i in range(n)]
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    arr[i]=max(arr[i],arr[j]+1)
        return max(arr)
'''