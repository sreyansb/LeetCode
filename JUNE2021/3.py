#attempt2:
class Solution:
    def maxArea(self, h: int, w: int, ho: List[int], ve: List[int]) -> int:
        ho.sort()
        ve.sort()
        horizontal=[0]
        horizontal+=ho
        horizontal+=[h]
        vertical=[0]
        vertical+=ve
        vertical+=[w]
        #print(horizontal)
        #print(vertical)
        maxh=0
        for i in range(1,len(horizontal)):
            maxh=max(maxh,horizontal[i]-horizontal[i-1])
        verh=0
        for i in range(1,len(vertical)):
            verh=max(verh,vertical[i]-vertical[i-1])
        #print(maxh,verh)
        return (maxh*verh)%((10**9)+7)

#attempt1:WA because didnt mod
'''
class Solution:
    def maxArea(self, h: int, w: int, ho: List[int], ve: List[int]) -> int:
        ho.sort()
        ve.sort()
        horizontal=[0]
        horizontal+=ho
        horizontal+=[h]
        vertical=[0]
        vertical+=ve
        vertical+=[w]
        #print(horizontal)
        #print(vertical)
        maxh=0
        for i in range(1,len(horizontal)):
            maxh=max(maxh,horizontal[i]-horizontal[i-1])
        verh=0
        for i in range(1,len(vertical)):
            verh=max(verh,vertical[i]-vertical[i-1])
        #print(maxh,verh)
        return (maxh*verh)
'''