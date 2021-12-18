#attempt1 : Had many non-submitted attempts
from bisect import bisect_right
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        leng = len(s)
        ans = [0]
        digits = ["0"]+digits
        diglen = len(digits)
        #print(leng,diglen)
        
        def digitdp(index,tight,p):
            #print(index,p,tight)
            if index>=leng:
                if p:
                    ans[0] += 1
                return
            
            newpos = bisect_right(digits,s[index])
            if p:
                start=1
            else:
                start=0
            
            if not tight:
                ans[0] += (diglen-1)**(leng-index)
                #can't simply do ans[0] += (diglen)**(leng-index)-1 as 0
                #could be preceeded by nonzero number if p==0
                if not p:
                    digitdp(index+1,tight,0)
                    
      
            else:
                for i in range(start,newpos):
                    digitdp(index+1,tight and not(digits[i]<s[index]),int(digits[i]))
        
        digitdp(0,True,0)
        return ans[0]
