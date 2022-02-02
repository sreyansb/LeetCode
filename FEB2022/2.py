#attempt2: 88ms
from collections import deque
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slen,plen = len(s),len(p)
        if plen>slen:
            return []
        curdi = {}
        pdic = {} 
        for i in range(ord('a'),ord('z')+1):
            chri = chr(i)
            curdi[chri] = 0
            pdic[chri] = 0
        for i in p:
            pdic[i] += 1
        #curdi = {}
        for i in range(plen):
            if s[i] not in curdi:
                curdi[s[i]] = 0
            curdi[s[i]] += 1
        ans = []
        
        if curdi==pdic:
            ans.append(0)
            
        for i in range(plen,slen):
            #start index of current string is i+1-plen
            curdi[s[i]] += 1
            curdi[s[i-plen]] -= 1
            if curdi==pdic:
                ans.append(i-plen+1)
            
        return ans

#attempt1: 258ms

from collections import deque
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slen,plen = len(s),len(p)
        if plen>slen:
            return []
        curdi = {}
        pdic = {}   
        for i in p:
            if i not in pdic:
                pdic[i] = 0
            pdic[i] += 1
        #curdi = {}
        for i in range(plen):
            if s[i] not in curdi:
                curdi[s[i]] = 0
            curdi[s[i]] += 1
        ans = []
        
        if curdi==pdic:
            ans.append(0)
            
        for i in range(plen,slen):
            #start index of current string is i+1-plen
            if s[i] not in curdi:
                curdi[s[i]] = 0
            curdi[s[i]] += 1
            curdi[s[i-plen]] -= 1
            if not(curdi[s[i-plen]]):
                del curdi[s[i-plen]]
            if curdi==pdic:
                ans.append(i-plen+1)
            
        return ans
    

