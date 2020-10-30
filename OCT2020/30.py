#attempt1: 15% -> get the number of ways to reach each element
#add it to get the value
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        lic=[1 for i in range(n)] #longest increasing sequence -> dp approach
        ans=[0 for i in range(n)]
        ans[0]=1
        for i in range(1,n):
            maxi=1
            count=1
            for j in range(i):
                if nums[i]>nums[j]:
                    lic[i]=max(lic[i],lic[j]+1)
                    if lic[i]>maxi:
                        maxi=lic[i]
                        count=ans[j]
                    elif lic[j]+1==maxi:
                        count+=ans[j]
            ans[i]=count
        ans[0]=1
        #print(lic,ans)
        answ=0
        maxie=max(lic)
        for i in range(n):
            if lic[i]==maxie:
                answ+=ans[i]
        return answ
"""     
        
