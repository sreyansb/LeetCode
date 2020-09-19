#attempt2: 99.74% 60%
#ans is not hardcoded
from bisect import bisect_right,bisect_left
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        noh=high
        nod=1
        while(noh):
            nod+=1
            noh//=10
        index=2
        ans=[]
        while(index<=nod):
            addition=int("1"*index)
            initi=int("".join(map(str,list(range(1,index+1)))))
            ind=0
            inj=10-index
            while(ind<inj):
                ans.append(initi)
                initi+=addition
                ind+=1
            index+=1
        inpos=bisect_left(ans,low)
        ops=bisect_right(ans,high)
        return ans[inpos:ops]

#attempt1: 95% 55%
"""
from bisect import bisect_right,bisect_left
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans=[12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]
        inpos=bisect_left(ans,low)
        ops=bisect_right(ans,high)
        return ans[inpos:ops]
"""
