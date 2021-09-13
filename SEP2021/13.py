#attempt1: "a" and "o" appear twice in "balloon"
#Therefore divide their occureneces by 2 
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        di={}
        for i in "balloon":
            di[i]=0
        for i in text:
            if i in "balloon":
                di[i]+=1
        mini=float('inf')
        for i in di:
            if i=="l" or i=="o":
                mini=min(mini,di[i]//2)
            else:
                mini=min(mini,di[i])
        return mini