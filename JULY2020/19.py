def addBinary(a, b):
        carry=0
        s=""
        al=len(a)
        bl=len(b)
        if al>bl:
            b="0"*(al-bl)+b
            bl=al
        elif bl>al:
            a="0"*(bl-al)+a
            al=bl
        for i in range(al-1,-1,-1):
            s=str(int(a[i])^int(b[i])^int(carry))+s
            carry=carry&(int(a[i])^int(b[i]))|(int(a[i])&int(b[i]))
            #print(s,carry,int(a[i])&int(b[i]))
        if carry:
            s=str(carry)+s
        return s
print(addBinary("1010","1011"))
#faster
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
            
        
        
