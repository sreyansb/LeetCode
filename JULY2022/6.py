#attempt1:
class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        f, s, t = 0, 1, 1
        n -= 1
        while(n):
            n -= 1
            t = f+s
            f = s
            s = t
        return t
        
