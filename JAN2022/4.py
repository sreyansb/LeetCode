#attempt1:
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        def recurse(number):
            if number == 0:
                return 0
            return (recurse(number>>1))*2 + (number&1)^1
        return recurse(n)
        
