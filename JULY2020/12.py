#first accepted solution
class Solution:
    def reverseBits(self,n):
        n=bin(n)[2:]
        return int(n[::-1]+'0'*(32-len(n)),2)

"""
#second accepted solution
class Solution:
    def reverseBits(self, n: int) -> int:
        s=""
        while(n):
            s+=str(n&1)
            n>>=1
        s=s+'0'*(32-len(s))
        return int(s,2)
"""



obj=Solution()
print(obj.reverseBits(43261596))

        
