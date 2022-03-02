#attempt2:
from bisect import bisect_right
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dit = {}
        for i in set(s):
            dit[i] = []
            
        n = len(t)
        
        for i in range(n):
            character = t[i]
            if character in dit:
                dit[character].append(i)
        
        prevpos = n
        for i in s[::-1]:
            #print(prevpos)
            pos = bisect_right(dit[i],prevpos)
            if pos == 0:
                return False
            prevpos = dit[i][pos-1]-1
        return True

#attempt1: WA : because I didn't subtract 1 from new prevpos
'''
from bisect import bisect_right
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dit = {}
        for i in set(s):
            dit[i] = []
            
        n = len(t)
        
        for i in range(n):
            character = t[i]
            if character in dit:
                dit[character].append(i)
        
        prevpos = n
        for i in s[::-1]:
            pos = bisect_right(dit[i],prevpos)
            if pos == 0:
                return False
            prevpos = dit[i][pos-1]
        return True
'''
