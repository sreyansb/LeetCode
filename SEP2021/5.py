#attempt3: TOOK HELP: It is quite simple:
#for k==1: it is a necklace
#for others it is basically sorted, check mathematical proof
'''
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        current=s
        s=list(s)
        if k==1:
            n=len(s)
            s=s+s[:-1]
            for i in range(n):
                if "".join(s[i:i+n])<current:
                    current="".join(s[i:i+n])
            return current
            
        current="".join(sorted(s))
        return current
'''

#attempt2:TLE Minor overlook error
#unsorted
'''
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        current=s
        s=list(s)
        a=min(s)
        while(True):
            current="".join(s)
            maxie=max(s[:k])
            s.pop(s.index(maxie))
            s+=[maxie]
            news="".join(s)
            if news>=maxie:
                break
        return current
        
'''

#attempt1:TOOK HELP.
#Funda based problem again.
# It seems I have tried this problem before

#TLE:Didn't take care of case when only single element exists in the string
#IDEA was also wrong : Thought of popping largest element in first k positions
#and adding at back and loop until current string <newly generated string

'''
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        current=s
        s=list(s)
        a=min(s)
        while(True):
            current="".join(s)
            maxie=max(s[:k])
            s.pop(s.index(maxie))
            s+=[maxie]
            news="".join(s)
            if news>maxie:
                break
        return current
'''


