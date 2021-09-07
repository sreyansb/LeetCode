#attempt3: AC
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

#attempt2:WA
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
        #print(ans,finans)
        ans=[list(i) for i in set(ans+finans)] 
        return ans
'''

#attempt1:Algo is called Jarvis March: We take leftmost point
#and try to find next point for which all other points are anti-clockwise 
# WA because along a line we see only the farthest point and not in
#between points
#Runtime error because didn't take care of division by zero error
# to find anticlockwise:- slope of p2-p1 <slope of p3-p1=>p3 is anticlockwise
#wrt p2
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
        finans=[]
        for i in range(1,len(ans)):
            p1,p2=ans[i-1],ans[i]
            for p3 in trees:
                if p3[1]-p1[1]==((p2[1]-p1[1])/(p2[0]-p1[0]))*(p3[0]-p1[0]):
                    finans.append(tuple(p3))
        #print(ans,finans)
        ans=[list(i) for i in set(ans+finans)] 
        return ans
'''