#attempt4: Accepted:TOOK help
#as we are calculating prefix sums check if the complement of the
#current prefix sum has appeared before in the dictionary
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        di={}
        i=0
        di[0]=1
        ans=0
        for j in nums:
            i+=j
            if i-k in di:
                ans+=di[i-k]
            if i not in di:
                di[i]=0
            di[i]+=1
        return ans

#attempt3: TLE 69/81
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=0
        for i in range(1,n):
            nums[i]+=nums[i-1]
        ans+=nums.count(k)
        for i in range(1,n):
            for j in range(i,n):
                ans+=1 if nums[j]-nums[i-1]==k else 0
        return ans
"""

#attempt2: TLE 69/81
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not(nums):
            return 0
        n=len(nums)
        ans=0
        sumarr=[nums[0]]
        for i in nums[1:]:
            sumarr.append(sumarr[-1]+i)
        ans+=sumarr.count(k)
        #print(sumarr)
        for i in range(1,n):
            for j in range(i,n):
                if sumarr[j]-sumarr[i-1]==k:
                    #print("g",i,j)
                    ans+=1
        return ans
"""

#attempt1: WA
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not(nums):
            return 0
        n=len(nums)
        ans=0
        sumarr=[nums[0]]
        for i in nums[1:]:
            sumarr.append(sumarr[-1]+i)
        ans+=sumarr.count(k)
        for i in range(1,n-1):
            for j in range(i+1,n):
                if sumarr[j]-sumarr[i-1]==k:
                    ans+=1
        return ans
"""
              
        
        
        
                
        
        
        
