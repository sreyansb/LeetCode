

#attempt2: 90% and 96%
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        bucket=[0 for i in range(len(nums)+1)]
        ans=[]
        for i in nums:
            bucket[i]+=1
            if bucket[i]==2:
                ans.append(i)
        return ans

#attempt1:Understood the question wrong wherein
# I thought one number has appeared twice and we need to find that
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        xor=0
        for i in nums:
            xor=xor^i
        for i in range(1,len(nums)+1):
            xor=xor^i
        return xor
'''