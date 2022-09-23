#attempt1:
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = ""
        for number in range(1,n+1):
            ans += bin(number)[2:]
        return int(ans,2)%(1000000007)
        
            
        
