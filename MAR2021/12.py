#attempt2:
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        for i in range(2**k):
            j=bin(i)[2:]
            j=j+"0"*(k-len(j))
            if j not in s:
                return False
        return True

#attempt1:
'''
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sn=set()
        for i in range(len(s)-k+1):
            sn.add(s[i:i+k])
        return len(sn)==2**k
'''
