#attempt2: 99% and 67%
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K%2==0 or K%5==0:
            return -1
        n=1
        index=1
        while(n%K!=0):
            index+=1
            n*=10
            n+=1
            n%=K
        return index

#attempt1: 25% and 86%
'''
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K%2==0 or K%5==0:
            return -1
        n=1
        index=1
        while(n%K!=0):
            index+=1
            n*=10
            n+=1
        return index
'''
