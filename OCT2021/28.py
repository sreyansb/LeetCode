#attempt2: Binary Search approach
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        for i in range(n):
            l = i+1
            r = n-1
            while(l<r):
                sumcur = nums[i]+nums[l]+nums[r]
                if sumcur==0:
                    ans.add(tuple(sorted([nums[i],nums[l],nums[r]])))
                    l += 1
                elif sumcur<0:
                    l += 1
                else:
                    r -= 1
        return [list(i) for i in ans]

#attempt1: 4736 ms - dict approach
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        for i in range(n):
            di = set()
            for j in range(i+1,n):
                if -nums[i]-nums[j] in di:
                    ans.add(tuple(sorted([nums[i],nums[j],-nums[i]-nums[j]])))
                di.add(nums[j])
        return ans
'''