#attempt1:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=0
        summy=0
        for i in nums:
            summy+=i
            n+=1
        return (n*(n+1))//2-summy
