#attempt1:
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        ans = 1
        highest = (1<<31)
        while(ans < highest):
            if ans == n:
                return True
            ans *= 3
        return False
        
