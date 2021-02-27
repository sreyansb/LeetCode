#attempt2:
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count="0"
        ans=1
        if divisor<0:
            divisor*=-1
            ans*=-1
        if dividend<0:
            dividend*=-1
            ans*=-1
        while(dividend>=divisor):
            ldi=len(str(divisor))
            newd=str(dividend)[ldi+1:]
            oldd=int(str(dividend)[:ldi+1])
            ncount=0
            while(oldd>=divisor):
                oldd-=divisor
                ncount+=1
            count+=str(ncount)
            dividend=int(str(oldd)+newd)
        count=int(count)*ans
        if count<2**31 and count>=-(2**31):
            return count
        return (2**31)-1
#attempt1: WA
#forgot to add 0 at last if string remains
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count="0"
        ans=1
        if divisor<0:
            divisor*=-1
            ans*=-1
        if dividend<0:
            dividend*=-1
            ans*=-1
        while(dividend>=divisor):
            ldi=len(str(divisor))
            newd=str(dividend)[ldi+1:]
            oldd=int(str(dividend)[:ldi+1])
            ncount=0
            while(oldd>=divisor):
                oldd-=divisor
                ncount+=1
            count+=str(ncount)
            dividend=int(str(oldd)+newd)
        count=int(count)*ans
        if count<2**31 and count>=-(2**31):
            return count
        return (2**31)-1
'''
