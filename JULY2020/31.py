#solved using f(n)=f(n-1)+f(n-2) and then solving the recursive function
class Solution:
    def climbStairs(self, n):
        if n==1:
            return 1
        x=5**0.5
        a1=2/(x*(x-1))
        a2=2*(x-2)/(3*x-5)
        #for i in range(1,46):
        #    print((a1*((1+x)/2)**i) + (a2*((1-x)/2)**i))
        return int((a1*((1+x)/2)**n) + (a2*((1-x)/2)**n))
obj=Solution()
print(obj.climbStairs(1))

#2nd attempt
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        x=1
        y=2
        z=0
        for i in range(2,n):
            z=x+y
            x=y
            y=z
        return z
"""
#1st attempt
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        x=1
        y=2
        z=0
        while(n>2):
            z=x+y
            x=y
            y=z
            n-=1
        return z
"""
