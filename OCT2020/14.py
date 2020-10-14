#attempt1: took hint that the computation should be between index 1 and n-2
#index 2 to n-1(because if we take index 1, n-1 cant be taken)-> 69% 
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        def dp(dpt,index,endindex):
            if index>endindex:
                return 0
            if dpt[index]!=-1:
                return dpt[index]
            dpt[index]=max(nums[index]+dp(dpt,index+2,endindex),dp(dpt,index+1,endindex))
            return dpt[index]
        dpt=[-1 for i in range(n)]
        val=dp(dpt,0,n-2)
        dpt=[-1 for i in range(n)]
        val1=dp(dpt,1,n-1)
        return max(val,val1)
        
            
        
