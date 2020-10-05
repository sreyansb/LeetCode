#attempt1:
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        st=""
        while(N):
            st=str((N%2)^1)+st
            N>>=1
        if st=="":
            st="1"
        return int(st,2)
        
