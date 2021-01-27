#attempt2:80%
from math import log2,floor
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod=10**9+7
        number=1
        for i in range(2,n+1):
            number=number<<floor(log2(i)+1)
            number+=i
            number%=mod
            #print(number)
        return number%mod

#attempt1: 31%
'''
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        st=""
        for i in range(1,n+1):
            st=st+bin(i)[2:]
        return int(st,2)%(10**9+7)
'''
