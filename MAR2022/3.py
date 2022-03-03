#attempt1:
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return 0
        differences = []
        for i in range(1,n):
            differences.append(nums[i]-nums[i-1])
        index = 0
        difflen = len(differences)
        ans = 0
        while(index<difflen):
            ele = differences[index]
            initindex = index
            while(index<difflen and differences[index]==ele):
                index += 1
            numbersequal = (index-1-initindex+1)
            ans += (numbersequal*(numbersequal-1))//2
        return ans
        
            
        
