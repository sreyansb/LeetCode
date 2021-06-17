#attempt3:
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        maxie=-1
        curlen=0
        ans=0
        indexoflast=-1
        for i in range(len(nums)):
            maxie=max(maxie,nums[i])
            if not(maxie<=right):
                maxie=-1
                curlen=0
                indexoflast=-1
                continue
            if maxie<left:
                curlen+=1
                continue
            if left<=nums[i]<=right:
                indexoflast=i
            curlen+=1
            startindex=i-curlen+1
            ans+=indexoflast-startindex+1
        return ans

#attempt2: WA 10/44 Realized that we dont need to restart when maxie<left but instead of adding elements to curlen I just continued
'''
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        maxie=-1
        curlen=0
        ans=0
        indexoflast=-1
        for i in range(len(nums)):
            maxie=max(maxie,nums[i])
            if not(maxie<=right):
                maxie=-1
                curlen=0
                indexoflast=-1
                continue
            if maxie<left:
                continue
            if left<=nums[i]<=right:
                indexoflast=i
            curlen+=1
            startindex=i-curlen+1
            ans+=indexoflast-startindex+1
        return ans
'''

#attempt1: WA 1/44 I dont know why I commented out the max part!
'''
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        maxie=-1
        curlen=0
        ans=0
        indexoflast=-1
        for i in range(len(nums)):
            #maxie=max(maxie,nums[i])
            if not(left<=maxie<=right):
                maxie=-1
                curlen=0
                indexoflast=-1
                continue
            if left<=nums[i]<=right:
                indexoflast=i
            curlen+=1
            startindex=i-curlen+1
            ans+=indexoflast-startindex+1
        return ans
'''