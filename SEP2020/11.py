#attempt 2 91%

#took help from geeks for geeks and also leetcode
#the max product can be a number, the max product for (i-1)th index*this number or this number * minimum of (i-1)th element* this -> when both are negative. 
#the min product can be this number, min of same as above
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxi = [0]*n
        mini = [0]*n
        maxi[0]=nums[0]
        mini[0]=nums[0]
        for i in range(1,n):
            maxi[i]=max(nums[i],maxi[i-1]*nums[i],mini[i-1]*nums[i])
            mini[i]=min(nums[i],maxi[i-1]*nums[i],mini[i-1]*nums[i])
        return max(maxi)

#Attempt 1 TLE 186/187
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        prods=[0]*n
        prods[-1]=nums[-1]
        for i in range(n-1):
            maxi=nums[i]
            prod=nums[i]
            for j in range(i+1,n):
                maxi=max(maxi,prod*nums[j])
                prod*=nums[j]
            prods[i]=maxi
        return max(prods) if prods else 0
"""               
                
            
            
            
        
        
