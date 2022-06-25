#attempt3: We need only adjacent element and not greatest
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        def recurse(endindex,notries,nums,adjacent):
            #print(nums)
            if endindex == 0:
                if notries <= 1:
                    return True
                return False
            if notries > 1:
                return False
            if nums[endindex-1] > nums[endindex]:
                ans = False
                if adjacent >= nums[endindex-1] or endindex == n-1:
                    ans = ans or recurse(endindex-1,notries+1,nums,nums[endindex])
                ans = ans or recurse(endindex-1,notries+1,nums[:endindex-1]+[nums[endindex]]+nums[endindex:],nums[endindex])
                return ans
            return recurse(endindex-1,notries,nums,nums[endindex])
        return recurse(n-1,0,nums,-float('inf'))
        
#attempt2: WA
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        def recurse(endindex,notries,nums,greatestonright):
            #print(nums)
            if endindex == 0:
                if notries <= 1:
                    return True
                return False
            if notries > 1:
                return False
            if nums[endindex-1] > nums[endindex]:
                ans = False
                if greatestonright >= nums[endindex-1] or endindex == n-1:
                    ans = ans or recurse(endindex-1,notries+1,nums,max(greatestonright,nums[endindex]))
                ans = ans or recurse(endindex-1,notries+1,nums[:endindex-1]+[nums[endindex]]+nums[endindex:],max(greatestonright,nums[endindex]))
                return ans
            return recurse(endindex-1,notries,nums,max(greatestonright,nums[endindex]))
        return recurse(n-1,0,nums,-float('inf'))
                
'''
#attempt1
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        def recurse(endindex,notries,nums,greatestonright):
            if endindex == 0:
                if notries <= 1:
                    return True
                return False
            if notries > 1:
                return False
            if nums[endindex-1] > nums[endindex]:
                ans = False
                if greatestonright >= nums[endindex-1]:
                    ans = ans or recurse(endindex-1,notries+1,nums,max(greatestonright,nums[endindex]))
                ans = ans or recurse(endindex-1,notries+1,nums[:endindex-1]+[nums[endindex]]+nums[endindex:],max(greatestonright,nums[endindex]))
                return ans
            return recurse(endindex-1,notries,nums,max(greatestonright,nums[endindex]))
        return recurse(n-1,0,nums,-float('inf'))
        
        
'''

