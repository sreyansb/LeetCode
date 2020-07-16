def findpow(x,n):
    if n==1:
        return x
    if n%2:
        return x*findpow(x*x,n>>1)
    else:
        return findpow(x*x,n>>1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n==1:
            return x
        if n<0:
            return 1/findpow(x,-n)
        else:
            return findpow(x,n)
        
