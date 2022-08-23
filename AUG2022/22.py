#attempt1:
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        number = 1
        highest = (1<<31)-1
        while(number <= highest):
            if n == number:
                return True
            number *= 4
        return False
        
