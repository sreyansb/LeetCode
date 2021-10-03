#attempt3:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        leng=len(nums)
        ans=[False for i in range(leng)]
        ans[-1]=True
        for i in range(leng-2,-1,-1):
            if i+nums[i]>=leng-1:
                ans[i]=True
            else:
                for j in range(i+nums[i],i,-1):
                    if ans[j]:
                        ans[i]=True
                        break
        return ans[0]

#attempt2: GOING opposite improved the performance
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastindex=len(nums)-1
        @lru_cache(None)
        def recurse(index):
            if index==lastindex:
                return True
            for i in range(min(lastindex,index+nums[index]),index,-1):
                ans=recurse(i)
                if ans:
                    return True
            return False
        return recurse(0)
'''

#attempt1:AC 
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastindex=len(nums)-1
        @lru_cache(None)
        def recurse(index):
            if index==lastindex:
                return True
            for i in range(index+1,index+nums[index]+1):
                ans=recurse(i)
                if ans:
                    return True
            return False
    
        return recurse(0)
'''