class Solution:
    def subsets(self, nums):
        finallist=[[]]
        for i in nums:
            finallist+=[[i]+cur for cur in finallist]
            
        return finallist

#MY SOLUTION-very slow
"""
def find1s(i,n):
    li=[]
    i=bin(i)[2:]
    i='0'*(n-len(i))+i
    for j in range(len(i)):
        if i[j]=='1':
            li.append(j)
    return li

class Solution:
    def subsets(self, nums):
        n=2**len(nums)
        n1=len(nums)
        finallist=[]
        for i in range(0,n):
            #print(i)
            x=[nums[j] for j in find1s(i,n1)]
            #print(x)
            finallist.append(x)
        return finallist
"""
nums=[1,2,3]
obj=Solution()
print(obj.subsets(nums))
            
            
