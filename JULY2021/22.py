#attempt2:
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n=len(nums)
        maxinl=[nums[0] for i in range(n)]
        mininr=[nums[-1] for i in range(n)]
        for i in range(1,n):
            maxinl[i]=max(maxinl[i-1],nums[i])
        for i in range(n-2,-1,-1):
            mininr[i]=min(mininr[i+1],nums[i])
        #print(maxinl,mininr)
        for i in range(n-1):
            if maxinl[i]<=mininr[i+1]:
                return i-0+1
        return n-1 

#attempt1: WA because didnt read properly, All elements to the left are <= right and not just <
#The minimum element to the right of the element should be greater than max of all the elements till this point
'''
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n=len(nums)
        maxinl=[nums[0] for i in range(n)]
        mininr=[nums[-1] for i in range(n)]
        for i in range(1,n):
            maxinl[i]=max(maxinl[i-1],nums[i])
        for i in range(n-2,-1,-1):
            mininr[i]=min(mininr[i+1],nums[i])
        #print(maxinl,mininr)
        for i in range(n-1):
            if maxinl[i]<mininr[i+1]:
                return i-0+1
        return n-1
'''