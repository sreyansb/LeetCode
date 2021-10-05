#attempt3: 24ms
class Solution:
    def climbStairs(self, n: int) -> int:
        f=1
        s=2
        t=-1
        if n<=2:
            return n
        for i in range(3,n+1):
            t=f+s
            f=s
            s=t
        return t

#attempt2:34ms
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        f=1
        s=2
        t=-1
        if n<=2:
            return n
        while(n>2):
            t=f+s
            f=s
            s=t
            n-=1
        return t
'''

#attempt1: 29ms
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        f=[1 for i in range(n+1)]
        if n==1:
            return 1
        f[2]=2
        if n<=2:
            return f[n]
        for i in range(3,n+1):
            f[i]=f[i-1]+f[i-2]
        return f[n]
'''