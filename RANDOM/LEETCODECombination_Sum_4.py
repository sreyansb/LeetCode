#attempt2: Took Help, instead of reaching to target reach 0
#use DP to solve
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans=[0]
        di={}#represents number of ways to reach target-x from x
        #=>di[0]=di[target-target] to reach target is 1
        di[0]=1
        def recurse(cursum):
            if cursum<0:
                return 0
            if cursum not in di:
                di[cursum]=0
                for num in nums:
                    di[cursum]+=recurse(cursum-num)
            return di[cursum]
                
        return recurse(target)

#attempt1: TLE
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans=[0]
        di={}
        def recurse(cursum):
            if cursum>target:
                return
            elif cursum==target:
                ans[0]+=1
            else:
                for i in nums:
                    recurse(i+cursum)
        recurse(0)
        return ans[0]
'''
