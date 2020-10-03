#ATTEMPT2: ACCEPTED: took help we need to sort an dbreak if difference becomes
#larger than k
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        di=set()
        n=len(nums)
        count=0
        nums.sort()
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[j]-nums[i]==k:
                    di.add((nums[i],nums[j]))
                elif nums[j]-nums[i]>k:
                    break
        return len(di)

#ATTEMPT1: TLE 52/59
"""
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans=set()
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                ansh=abs(nums[i]-nums[j])
                if ansh==k:
                    ans.add(tuple(sorted([nums[i],nums[j]])))
        return len(ans)
"""       
