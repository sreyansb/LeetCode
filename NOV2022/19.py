#attempt2: COPIED didn't even understand
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        
        def crossProduct(p1,p2,p3):
            ### V1 = (a,b), V2 = (c,d)
            ### V1 X V2 = a*d - b*c
            a = p2[0]-p1[0]
            b = p2[1]-p1[1]
            c = p3[0]-p1[0]
            d = p3[1]-p1[1]
            return a*d - b*c
        
        def constructHalfHull(points):
            stack = []
            for p in points:
                ### if the chain formed by the current point
                ### and the last two points in the stack is not counterclockwise, pop it
                while len(stack)>=2 and crossProduct(stack[-2],stack[-1],p)>0:
                    stack.pop()
                ### append the current point.
                stack.append(tuple(p))
            return stack
        
        ### sort points by x, so we are moving from left to right
        points.sort()
        leftToRight = constructHalfHull(points)
        ### reverse points, so we are moving from right to left
        rightToLeft = constructHalfHull(points[::-1])
        
        ### it is posible that the top and bottom parts have same points (e.g., all points form a line)
        ### we remove the duplicated points using a set
        return list(set(leftToRight + rightToLeft))

#attempt1: TLE copied previous AC solution
'''
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        n=len(trees)
        if n<4:
            return trees
        l=0
        for i in range(1,n):
            if trees[i][0]<trees[l][0]:
                l=i
        flag=1
        p=l
        ans=[]
        
        def CCW(p1,p2,p3):
            if (p2[1]-p1[1])*(p3[0]-p1[0])<(p3[1]-p1[1])*(p2[0]-p1[0]):
                return True
            return False
        
        while(True):
            flag=0
            ans.append(tuple(trees[p]))
            q=(p+1)%n
            
            for i in range(n):
                if CCW(trees[p],trees[i],trees[q]):
                    q=i
                        
            p=q
            if p==l:
                break
        #ans.pop()
        print(ans)
        finans=[]
        for i in range(1,len(ans)):
            p1,p2=ans[i-1],ans[i]
            for p3 in trees:
                try:
                    if p3[1]-p1[1]==((p2[1]-p1[1])/(p2[0]-p1[0]))*(p3[0]-p1[0]):
                        finans.append(tuple(p3))
                except:
                    if p2[0]==p3[0]:
                        finans.append(tuple(p3))
        p1,p2=ans[0],ans[-1]
        for p3 in trees:
            try:
                if p3[1]-p1[1]==((p2[1]-p1[1])/(p2[0]-p1[0]))*(p3[0]-p1[0]):
                    finans.append(tuple(p3))
            except:
                if p2[0]==p3[0]:
                    finans.append(tuple(p3))
        #print(ans,finans)
        ans=[list(i) for i in set(ans+finans)] 
        return ans
            
            
        
'''
