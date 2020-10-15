#ATTEMPT2: constant space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        def doreverse(start,end):
            while(start<=end):
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        doreverse(n-k,n-1)
        #print(nums)
        doreverse(0,n-k-1)
        #print(nums)
        doreverse(0,n-1)

#Attempt1: not constant space
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        newarr=nums[n-k:]+nums[:n-k]
        for i in range(n):
            nums[i]=newarr[i]
""" 
