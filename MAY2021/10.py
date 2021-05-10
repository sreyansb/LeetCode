#attempt4:
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1 or n==2:
            return 0
        li=[1 for i in range(n)]
        count=0
        li[0]=0
        li[1]=0
        for p in range(2,int(n**0.5)+1):
            if li[p]:
                count+=1
                for j in range(p*p,n,p):
                    li[j]=0
        return sum(li)
'''

#attempt1:
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        li=[1 for i in range(n)]
        li[0]=0
        li[1]=0
        for p in range(2,n):
            if li[p]:
                for j in range(p*p,n,p):
                    li[j]=0
        return len([i for i in li if i])
'''
