#attempt1: 90.41%
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not(nums):
            return []
        ans=[]
        n=len(nums)
        diff=[]
        for i in range(1,n):
            diff.append(nums[i]-nums[i-1])
        start=0
        init=""
        for i in range(n-1):
            if init=="":
                init=str(nums[start])
            if diff[i]==1:
                continue
            else:
                if nums[i]==nums[start]:
                    init=init
                else:
                    init=init+"->"+str(nums[i])
                ans.append(init)
                init=""
                start=i+1
        if init:
            if nums[start]==nums[-1]:
                ans.append(init)
            else:
                ans.append(init+"->"+str(nums[-1]))
        else:
            ans.append(str(nums[-1]))
        return ans
                
            
            
            
                
                    
                
            
        
