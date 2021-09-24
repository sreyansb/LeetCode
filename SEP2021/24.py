#attempt1:
class Solution:
    def tribonacci(self, n: int) -> int:
        f=[0,1,1]
        if n<=2:
            return f[n]
        n-=2
        while(n):
            f.append(f[-1]+f[-2]+f[-3])
            n-=1
        return f[-1]
        