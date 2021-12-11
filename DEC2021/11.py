#attempt1: TOOK HELP, this is just pure math and binary search
from math import lcm
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        high = n*max(a,b)
        low = min(a,b)
        lcmab = lcm(a,b)
        while(high>=low):
            mid = (high+low)//2
            if mid//a+mid//b-mid//(lcmab)<n:
                low = mid+1
            else:
                high = mid-1
        return low%(1000000007)
                
        
