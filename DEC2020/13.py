#attempt3:TOOK HELP, great problem
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #took help top down approach
        #fix a place and find via dp and memoization the solution for left and right half
        nums=[1]+nums+[1]
        dpt={}
        def dp(l,r):#get the value of the dp without including left and right
            if l==r-1:
                return 0
            if (l,r) not in dpt:
                dpt[(l,r)]=max([dp(l,i)+nums[l]*nums[r]*nums[i]+dp(i,r) for i in range(l+1,r)])
            return dpt[(l,r)]
        return dp(0,len(nums)-1)
            
        
'''

#attempt2: Recursion TLE 24/70 [7,9,8,0,7,1,3,5,5,2,3] n! time
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def recurse(nums):
            #print(nums)
            if not(nums):
                return 0
            if len(nums)==1:
                return nums[0]
            if len(nums)==2:
                return nums[0]*nums[1]+max(nums)
            copied=[1]+nums+[1]
            n=len(copied)
            maxi=-float('inf')
            for i in range(1,n-1):
                k=nums.pop(i-1)
                ans=copied[i-1]*copied[i]*copied[i+1]+recurse(nums)
                nums.insert(i-1,k)
                maxi=max(maxi,ans)
            return maxi
        return recurse(nums)

        
'''

#attempt1: WA -> Wrong Concept Thought that answer should
#be middle nummbers and finally last and first element
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        sumi=0
        while(nums):
            if len(nums)==1:
                sumi+=nums[0]
                nums.pop(0)
            elif len(nums)==2:
                sumi+=nums[0]*nums[1]+max(nums)
                nums=[]
            else:
                mini=nums.index(min(nums[1:-1]))
                sumi+=nums[mini-1]*nums[mini]*nums[mini+1]
                nums.pop(mini)
        return sumi
        
'''
