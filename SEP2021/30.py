#attempt2:
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        n=len(nums)
        if sum(nums)%k:
            return False
        sumr=sum(nums)//k
        for i in nums:
            if i>sumr:
                return False
        def recurse(index,sumarr):
            if index>=n:
                return set(sumarr)=={sumr}
            for i in sumarr:
                if i>sumr:
                    return False
            ans=False
            for i in range(k):
                sumarr[i]+=nums[index]
                ans=ans or recurse(index+1,sumarr)
                sumarr[i]-=nums[index]
                if ans:
                    break
            return ans
        return recurse(0,[0]*k)
            
        

#attempt1:
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        n=len(nums)
        if sum(nums)%k:
            return False
        sumr=sum(nums)//k
        
        def recurse(index,sumarr):
            if index>=n:
                return set(sumarr)=={sumr}
            for i in sumarr:
                if i>sumr:
                    return False
            ans=False
            for i in range(k):
                sumarr[i]+=nums[index]
                ans=ans or recurse(index+1,sumarr)
                sumarr[i]-=nums[index]
                if ans:
                    break
            return ans
        return recurse(0,[0]*k)
            
        