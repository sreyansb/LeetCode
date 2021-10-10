#attempt2:
from math import ceil,log2
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left==0:
            return 0
        
        if ceil(log2(right+1))>ceil(log2(left+1)):
            return 0
        reqddigits=ceil(log2(right+1))
        binr=str(bin(right))[2:]
        binl=str(bin(left))[2:]
        i=0
        while(i<reqddigits and binr[i]==binl[i]):
            i+=1
        return int(binr[:i]+"0"*(reqddigits-i),2)

#attempt1: Runtime Error because for a number of the form 2^n, number of 
#bits is n+1 but with ceil(log2) we would only get n bits and give wrong results
'''
from math import ceil,log2
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left==0:
            return 0
        if ceil(log2(right+1))>ceil(log2(left+1)):
            return 0
        reqddigits=ceil(log2(right))
        binr=str(bin(right))[2:]
        binl=str(bin(left))[2:]
        
        i=0
        while(i<reqddigits and binr[i]==binl[i]):
            i+=1
        return int(binr[:i]+"0"*(reqddigits-i),2)
'''