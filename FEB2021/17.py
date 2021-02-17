#attempt2: Took Help  :- It is a 2 ptr problem. Go from left to right(maximize
#breadth). Assume the first ptr points to the highest height waala bar and the
#right waala ptr points to the smaller edge.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        f,e=0,len(height)-1
        maxar=-float('inf')
        while(f<=e):
            maxar=max(maxar,min(height[f],height[e])*abs(f-e))
            if height[f]<=height[e]:
                f+=1
            else:
                e-=1
        return maxar
        

#attempt1:Wrong answer Couldnt understand
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        h1=max(height)
        i1=height.index(h1)
        h2=0
        try:
            h2=max(height[:i1])
            h2=max(h2,max(height[i1+1:]))
        except:
            h2=max(h2,max(height[i1+1:]))
        i2=height.index(h2)
        maxar=abs(h2*(i2-i1))
        l1=i1-1
        n=len(height)
        while(l1>=0):
            if height[l1]>=height[i2]:
                maxar=max(maxar,height[i2]*abs(l1-i2))
            maxar=max(maxar,height[l1]*abs(l1-i1))
            l1-=1
        l1=i1+1
        while(l1<n):
            if height[l1]>=height[i2]:
                maxar=max(maxar,height[i2]*abs(l1-i2))
            maxar=max(maxar,height[l1]*abs(l1-i1))
            l1+=1
        return maxar
        
'''
