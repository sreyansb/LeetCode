#attempt1:
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        mins=[float('inf')]*n
        mins[-1]=0
        for i in range(n-2,-1,-1):
            if n-1-i<=nums[i]:
                mins[i]=1
            for j in range(i+1,min(n-1,i+nums[i])+1):
                mins[i]=min(mins[i],1+mins[j])
        return mins[0]
                
