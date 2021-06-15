#attempt1:
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summy=sum(nums)
        if summy%k:
            return False
        nums.sort(reverse=True)
        reqd=summy//k
        n=len(nums)
        def check(index,arr,maxie):
            if index>=n:
                return len(set(arr))==1
            if maxie>reqd:
                return False
            for i in range(k):
                arr[i]+=nums[index]
                ans=check(index+1,arr,max(maxie,arr[i]))
                if ans:
                    return True
                arr[i]-=nums[index]
            return False
        return check(0,[0]*k,0)
        #print(ans)
        '''
        if sum(nums)%k:
            return False
        n=sum(nums)//k
        sums=[n for i in range(k)]
        for i in nums:
            for j in range(k):
                if sums[j]>=i:
                    sums[j]-=i
                    break
        return sums==[0 for i in range(k)]
        '''
                
        