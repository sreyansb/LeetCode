#attempt2: Had to take help
#it is a bit masking problem
#we get the MSB and solve
class Solution:
    def findMaximumXOR(self, nums):
        maxi=0
        mask=0
        for i in range(31,-1,-1):
            se=set()
            mask|=1<<i
            newmax=maxi|1<<i
            print("m",mask)
            print("nm",newmax)
            for j in nums:
                se.add(j&mask)
            for j in se:
                if j^newmax in se:
                    print("yes  ",j,j^newmax)
                    maxi=newmax
                    break
            print("max",maxi)
        return maxi
obj=Solution()
print(obj.findMaximumXOR([3,10,5,25,2,8,100,101]))
        

#attempt1: TLE O(n^2) algo
"""
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxi=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                maxi=max(maxi,nums[i]^nums[j])
        return maxi
"""
