#attempt3:
class Solution:
    def maxPower(self, s: str) -> int:
        maxi = 1
        curlen = 0
        prevchar = 5
        for index in range(len(s)):
            i = s[index]
            if i!=prevchar:
                maxi = max(maxi,curlen)
                curlen = 1
                prevchar = i
            else:
                curlen += 1
        return max(maxi,curlen)
        

#attempt2: AC 44ms
'''
class Solution:
    def maxPower(self, s: str) -> int:
        maxi = 1
        previndex = 1
        prevchar = 5
        for index in range(len(s)):
            i = s[index]
            if i!=prevchar:
                maxi = max(maxi,index-1-previndex+1)
                previndex = index
                prevchar = i
        return max(maxi,len(s)-1-previndex+1)
        
'''

#attempt1: WA because didn't take care of cases like "cc"
'''
class Solution:
    def maxPower(self, s: str) -> int:
        maxi = 1
        previndex = 1
        prevchar = 5
        for index in range(len(s)):
            i = s[index]
            if i!=prevchar:
                maxi = max(maxi,index-1-previndex+1)
                previndex = index
                prevchar = i
        return maxi
'''
