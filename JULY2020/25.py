#2nd attempt with help:
class Solution:
    def findMin(self, a: List[int]) -> int:
        ans=0
        ansh=len(a)-1
        while(ans<ansh):
            mid=(ans+ansh)//2
            if a[mid]==a[ans]==a[ansh]:
                ans+=1
                ansh-=1
            elif a[ansh]>=a[mid]:
                ansh=mid
            else:
                ans=mid+1
        return a[ans]

"""
#1st attempt
class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=0
        for i in range(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                ans=i+1
                break
        return nums[ans]
"""       
        
