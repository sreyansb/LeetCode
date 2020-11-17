#attempt3: 80%->lattice problem
class Solution:
    def mirrorReflection(self, p, q):
        while(p%2==0 and q%2==0):
            p//=2
            q//=2
        if p%2:
            if q%2:
                return 1
            else:
                return 0
        else:
            if q%2:
                return 2

#attempt2: 20%
'''
from math import floor,ceil
class Solution:
    def mirrorReflection(self, p, q):
        points=[(p,0),(p,p),(0,p)]
        curh=0
        curw=0
        k=q/p
        kin=p/q
        remh=p
        up=1
        while((curw,curh) not in points):
            if remh>=q:
                curh=curh+up*q
                curw=0 if curw==p else p
                remh-=q
            else:
                if up==1:
                    up*=-1
                    curw=p if curw==0 else 0
                    remh=p*k-remh
                    curh=p-remh
                else:
                    curh=p*k-curh
                    up=1
                    curw=p if curw==0 else 0
                    remh=p-curh
            curh=floor(curh) if curh-floor(curh)<ceil(curh)-curh else ceil(curh)
            curw=floor(curw) if curw-floor(curw)<ceil(curw)-curw else ceil(curw)
            remh=floor(remh) if remh-floor(remh)<ceil(remh)-remh else ceil(remh)
            #print(curw,curh)
        return points.index((curw,curh))
'''
#attempt1: TLE
"""
class Solution:
    def mirrorReflection(self, p, q):
        points=[(p,0),(p,p),(0,p)]
        curh=0
        curw=0
        k=q/p
        kin=p/q
        remh=p
        up=1
        while((curw,curh) not in points):
            if remh>=q:
                curh=curh+up*q
                curw=0 if curw==p else p
                remh-=q
            else:
                if up==1:
                    up*=-1
                    curw=p if curw==0 else 0
                    remh=p*k-remh
                    curh=p-remh
                else:
                    curh=p*k-curh
                    up=1
                    curw=p if curw==0 else 0
                    remh=p-curh
            
            #print(curw,curh)
        return points.index((curw,curh))
"""
obj=Solution()
print(obj.mirrorReflection(45,26))

                    
                    
                    
                    
                
