#attempt1:
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n<2:
            return n
        nums=[0,1]
        k=2
        while(k<=n):
            if k%2:
                index=(k-1)//2
                nums.append(nums[index]+nums[index+1])
            else:
                nums.append(nums[k//2])
            k+=1
        return max(nums)
        
        
