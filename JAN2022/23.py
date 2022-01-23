#attempt4: 36ms, we need just one call for high, then sort it and do bisect_left
#on low
from bisect import bisect_left
from sortedcontainers import SortedList
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def digit_dp(curnumber,limit,ans):
            if curnumber>limit:
                return
            
            ans.add(curnumber)
            
            if curnumber==0:
                for i in range(1,10):
                    digit_dp(i,limit,ans)
            else:
                lastdigit = int(str(curnumber)[-1])
                if lastdigit!=9:
                    digit_dp(curnumber*10+lastdigit+1,limit,ans)
            
            return
        
        ansb = SortedList()
        
        digit_dp(0,high,ansb)
        #ansb = sorted(ansb)
        pos = ansb.bisect_left(low)
        return ansb[pos:]

#attempt3: 53ms
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def digit_dp(curnumber,limit,ans):
            if curnumber>limit:
                return
            
            ans.add(curnumber)
            
            if curnumber==0:
                for i in range(1,10):
                    digit_dp(i,limit,ans)
            else:
                lastdigit = int(str(curnumber)[-1])
                if lastdigit!=9:
                    digit_dp(curnumber*10+lastdigit+1,limit,ans)
            
            return
        
        anss = set()
        ansb = set()
        
        digit_dp(0,low,anss)
        digit_dp(0,high,ansb)
        final = {low}
        slow = str(low)
        for i in range(1,len(slow)):
            if int(slow[i]) != int(slow[i-1])+1:
                final.remove(low)
                break
        return sorted((ansb-anss)|final)        

#attempt2: WA: wrong check : if sorted(str(low)) == str(low), doesn't mean that
#low is sequential
'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def digit_dp(curnumber,limit,ans):
            if curnumber>limit:
                return
            
            ans.add(curnumber)
            
            if curnumber==0:
                for i in range(1,10):
                    digit_dp(i,limit,ans)
            else:
                lastdigit = int(str(curnumber)[-1])
                if lastdigit!=9:
                    digit_dp(curnumber*10+lastdigit+1,limit,ans)
            
            return
        
        anss = set()
        ansb = set()
        
        digit_dp(0,low,anss)
        digit_dp(0,high,ansb)
        final = {low} if sorted(str(low)) == list(str(low)) else set()
        return sorted((ansb-anss)|final)
'''

#attempt1:WA - What if low itself is sequential? Will be removed because of
#set intersection
'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def digit_dp(curnumber,limit,ans):
            if curnumber>limit:
                return
            
            ans.add(curnumber)
            
            if curnumber==0:
                for i in range(1,10):
                    digit_dp(i,limit,ans)
            else:
                lastdigit = int(str(curnumber)[-1])
                if lastdigit!=9:
                    digit_dp(curnumber*10+lastdigit+1,limit,ans)
            
            return
        
        anss = set()
        ansb = set()
        
        digit_dp(0,low,anss)
        digit_dp(0,high,ansb)
        return sorted(ansb-anss)
'''
