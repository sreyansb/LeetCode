#attempt2: 60% and 97%
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=sorted(s)
        t=sorted(t)
        index=0
        while(index<len(s)):
            if s[index]!=t[index]:
                return t[index]
            index+=1
        return t[-1]
        

#attempt1: 25% and 68%
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        di={}
        for i in t:
            if i not in di:
                di[i]=0
            di[i]+=1
        for j in s:
            di[j]-=1
        for i in di:
            if di[i]:
                return i
"""       
