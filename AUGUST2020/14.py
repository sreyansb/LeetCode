class Solution:
    def longestPalindrome(self, s: str) -> int:
        di={}
        for i in s:
            if i not in di:
                di[i]=0
            di[i]+=1
        k=sorted(di.keys(),key=lambda x:di[x]%2)
        #s=""
        leni=0
        isodd=1
        for i in k[::-1]:
            if isodd and di[i]%2:
                isodd=0
                #s=i*di[i]
                leni=di[i]
            else:
                #s=i*(di[i]>>1)+s+i*(di[i]>>1)
                leni+=2*(di[i]>>1)
        return leni
            
        
