#attempt3:
from itertools import permutations
from math import log2
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        def checkfor2(li):
            if li[0]!='0':
                number=int("".join(li))
                k=log2(number)
                return k==int(k)
            return False
        li=permutations(str(N),len(str(N)))
        ans=False
        for i in li:
            ans=checkfor2(list(i))
            if ans:
                break
        return ans

#attempt2: TLE in first attempt, replace logn for number of bits with logn
#from math directly
'''
from math import log2
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        def checkpowerof2(li):
            if li[0]!='0':
                number=int("".join(li))
                k=log2(number)
                return k==int(k)
            return False
        def recurse(l,r):
            if l==r:
                if checkpowerof2(a):
                    return True
                return False
            ans=False
            for i in range(l,r+1):
                a[l],a[i]=a[i],a[l]
                ans=recurse(l+1,r)
                if ans:
                    break
                a[l],a[i]=a[i],a[l]
            return ans
        a=list(str(N))
        return recurse(0,len(a)-1)
'''
