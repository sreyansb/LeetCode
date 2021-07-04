#attempt3: AC do mod at each step of calculation
from functools import lru_cache
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod=1000000007
        @lru_cache(None)
        def count(n,parent):
            if n==1:
                return 1
            co=0
            if parent=="a":
                co=count(n-1,"e")
            if parent=="e":
                co+=count(n-1,"a")
                co+=count(n-1,"i")
            if parent=="i":
                co+=count(n-1,"a")
                co+=count(n-1,"e")
                co+=count(n-1,"o")
                co+=count(n-1,"u")
            if parent=="o":
                co+=count(n-1,"i")
                co+=count(n-1,"u")
            if parent=="u":
                co+=count(n-1,"a")
            
            return co%mod
        counter=0
        for i in ["a","e","i","o","u"]:
            counter+=count(n,i)
        return counter%(mod)
            

#attempt1: MEmory error and TLE DOnt have to maintain the solutions
'''
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dpt={}
        def count(n,parent):
            if n==1:
                return 1
            if (n,parent) in dpt:
                return dpt[(n,parent)]
            co=0
            if parent=="a":
                co+=count(n-1,"e")
            if parent=="e":
                co+=count(n-1,"a")
                co+=count(n-1,"i")
            if parent=="i":
                co+=count(n-1,"a")
                co+=count(n-1,"e")
                co+=count(n-1,"o")
                co+=count(n-1,"u")
            if parent=="o":
                co+=count(n-1,"i")
                co+=count(n-1,"u")
            if parent=="u":
                co+=count(n-1,"a")
            dpt[(n,parent)]=co
            return co
        counter=0
        for i in ["a","e","i","o","u"]:
            counter+=count(n,i)
        return counter%(1000000007)
'''