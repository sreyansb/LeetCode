#attempt1:
class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        while(num):
            new = 0
            while(num):
                new += num%10
                num //= 10
            ans = new
            if new>=10:
                num = new
        return ans
                
            
        
