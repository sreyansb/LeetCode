#attempt3: other 2 are WA for n==0
class Solution:
    def isUgly(self, n: int) -> bool:
        ans = True
        if n == 0:
            return False
        while(n):
            if n&1 == 0:
                n //= 2
            else:
                if n%3 == 0:
                    n //= 3
                elif n%5 == 0:
                    n //= 5
                else:
                    ans = n == 1
                    break
        return ans
