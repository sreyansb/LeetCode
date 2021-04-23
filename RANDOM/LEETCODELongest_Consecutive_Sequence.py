#attempt1: remember the main test case with one element
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=sorted(nums)
        index=0
        n=len(nums)
        if n==0:
            return 0
        ans=1
        while(index<n-1):
            j=index+1
            leng=1
            while(j<n and nums[j]==nums[j-1]+1):
                leng+=1
                j+=1
            ans=max(ans,leng)
            index=j
        return ans
                
            
        
        
