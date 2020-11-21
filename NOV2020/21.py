#attempt_final:
from bisect import bisect_right
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        lenp=len(str(n))
        lend=len(digits)
        index=1
        ans=0
        while(index<lenp):
            ans+=lend**index
            index+=1
        digits.sort()
        nstr=str(n)
        lenp-=1
        pos=bisect_right(digits,(nstr[0]))
        if digits[pos-1]<(nstr[0]):
            ans+=(pos)*(lend**lenp)
            return ans
        elif lenp==0 and digits[pos-1]==nstr[0]:
            ans+=(pos)*(lend**lenp)
            return ans
        elif digits[pos-1]==nstr[0]:
            if pos==0:
                return ans
            ans+=(pos-1)*(lend**lenp)
            for i in nstr[1:]:
                lenp-=1
                k=(i)
                pos1=bisect_right(digits,k)
                if pos1==0:
                    return ans
                if digits[pos1-1]<i:
                    ans+=(pos1)*(lend**lenp)
                    return ans
                elif digits[pos1-1]==i and lenp==0:
                    ans+=(pos1-1)*(lend**lenp)+1
                elif digits[pos1-1]==i:
                    ans+=(pos1-1)*(lend**lenp)
                #print(i,ans)
            return ans
        return ans

#attempts before:
"""
from bisect import bisect_right
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        lenp=len(str(n))
        lend=len(digits)
        index=1
        ans=0
        while(index<lenp):
            ans+=lend**index
            index+=1
        digits.sort()
        nstr=str(n)
        lenp-=1
        pos=bisect_right(digits,(nstr[0]))
        if digits[pos-1]<(nstr[0]):
            ans+=(pos)*(lend**lenp)
            return ans
        elif lenp==0 and digits[pos-1]==nstr[0]:
            ans+=(pos)*(lend**lenp)
            return ans
        elif digits[pos-1]==nstr[0]:
            if pos==0:
                return ans
            ans+=(pos-1)*(lend**lenp)
            for i in nstr[1:]:
                lenp-=1
                k=(i)
                pos1=bisect_right(digits,k)
                if pos1==0:
                    return ans
                if digits[pos1-1]<i:
                    ans+=(pos1)*(lend**lenp)
                elif digits[pos1-1]==i and lenp==0:
                    ans+=(pos1-1)*(lend**lenp)+1
                elif digits[pos1-1]==i:
                    ans+=(pos1-1)*(lend**lenp)
                #print(i,ans)
            return ans
        return ans
"""
