#attempt1:
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while(n):
            ans += 1
            n &= n-1
        return ans
        
