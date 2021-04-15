#attempt1:
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        fir=0
        sec=1
        n-=1
        while(n):
            fir,sec=sec,fir+sec
            n-=1
        return sec
        
