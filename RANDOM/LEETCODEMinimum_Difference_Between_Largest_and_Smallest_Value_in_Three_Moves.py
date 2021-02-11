#attempt1: Took help, didnt know how to solve
#we need to take out atmost 3 elements either from beginning or end of sorted array
'''
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        def recurse(lindex,rindex,nodeleted):
            if nodeleted==3:
                return nums[rindex]-nums[lindex]
            return min(recurse(lindex+1,rindex,nodeleted+1),recurse(lindex,rindex-1,nodeleted+1))
        nums.sort()
        if len(nums)<=4:
            return 0
        return recurse(0,len(nums)-1,0)
'''
