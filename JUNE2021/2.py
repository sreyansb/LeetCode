#attempt3:AC 82% memoized
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1+s2==s3 or s2+s1==s3:
            return True
        n=len(s1)
        m=len(s2)
        tot=len(s3)
        if n+m!=tot:
            return False
        dp={}
        def check(p1,p2,f,val=[0,0],parent=-1):
            if abs(val[0]-val[1])>1:
                return False
            if f==tot:
                return True
            if p1==n:
                if s2[p2:]==s3[f:] and abs(val[1]+1-val[0])<=1:
                    return True
                return False
            if p2==m:
                if s1[p1:]==s3[f:] and abs(val[0]+1-val[1])<=1:
                    return True
                return False
            if (p1,p2,f,parent) in dp:
                return dp[(p1,p2,f,parent)]
            dp[(p1,p2,f,parent)]=False
            if s3[f]==s1[p1] and s3[f]==s2[p2]:
                ans=False
                if parent==1:
                    ans=check(p1+1,p2,f+1,[val[0]+1,val[1]],0)
                else:
                    ans=check(p1+1,p2,f+1,[val[0],val[1]],0)
                if ans:
                    dp[(p1,p2,f,parent)]=True
                    return True
                if parent==0:
                    ans=check(p1,p2+1,f+1,[val[0],val[1]+1],1)
                else:
                    ans=check(p1,p2+1,f+1,[val[0],val[1]],1)
                dp[(p1,p2,f,parent)]=ans
                return ans
            if s3[f]==s1[p1]:
                ans=False
                if parent==1:
                    ans = check(p1+1,p2,f+1,[val[0]+1,val[1]],0)
                else:
                    ans= check(p1+1,p2,f+1,val,0)
                dp[(p1,p2,f,parent)]=ans
                return ans
            if s3[f]==s2[p2]:
                ans=False
                if parent==0:
                    ans=check(p1,p2+1,f+1,[val[0],val[1]+1],1)
                else:
                    ans=check(p1,p2+1,f+1,[val[0],val[1]],1)
                dp[(p1,p2,f,parent)]=ans
                return ans
            return dp[(p1,p2,f,parent)]
        return check(0,0,0,[0,0])

#attempt2:TLE Trying DP now
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1+s2==s3 or s2+s1==s3:
            return True
        n=len(s1)
        m=len(s2)
        tot=len(s3)
        if n+m!=tot:
            return False
        def check(p1,p2,f,val=[0,0],parent=-1):
            if abs(val[0]-val[1])>1:
                return False
            if f==tot:
                return True
            if p1==n:
                if s2[p2:]==s3[f:] and abs(val[1]+1-val[0])<=1:
                    return True
                return False
            if p2==m:
                if s1[p1:]==s3[f:] and abs(val[0]+1-val[1])<=1:
                    return True
                return False
            if s3[f]==s1[p1] and s3[f]==s2[p2]:
                ans=False
                if parent==1:
                    ans=check(p1+1,p2,f+1,[val[0]+1,val[1]],0)
                else:
                    ans=check(p1+1,p2,f+1,[val[0],val[1]],0)
                if ans:
                    return True
                if parent==0:
                    ans=check(p1,p2+1,f+1,[val[0],val[1]+1],1)
                else:
                    ans=check(p1,p2+1,f+1,[val[0],val[1]],1)
                return ans
            if s3[f]==s1[p1]:
                if parent==1:
                    return check(p1+1,p2,f+1,[val[0]+1,val[1]],0)
                else:
                    return check(p1+1,p2,f+1,val,0)
            if s3[f]==s2[p2]:
                if parent==0:
                    return check(p1,p2+1,f+1,[val[0],val[1]+1],1)
                else:
                    return check(p1,p2+1,f+1,[val[0],val[1]],1)
            return False
        return check(0,0,0,[0,0])
'''

#attempt1:WA because I am seeing until the character matches, move it
# could be that the next matching character comes in the other string
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1+s2==s3 or s2+s1==s3:
            return True
        n=len(s1)
        m=len(s2)
        tot=len(s3)
        if n+m!=tot:
            return False
        def check(p1,p2,f,val=[0,0]):
            if abs(val[0]-val[1])>1:
                return False
            if f==tot:
                return True
            if p1==n:
                if s2[p2:]==s3[f:] and abs(val[1]+1-val[0])<=1:
                    return True
                return False
            if p2==m:
                if s1[p1:]==s3[f:] and abs(val[0]+1-val[1])<=1:
                    return True
                return False
            if s3[f]==s1[p1] and s3[f]==s2[p2]:
                ans=False
                p1c,p4=p1,f
                while(f<tot and p1<n and s3[f]==s1[p1]):
                    p1+=1
                    f+=1
                ans=ans or check(p1,p2,f,[val[0]+1,val[1]])
                if ans:
                    return True
                while(p4<tot and p2<m and s3[p4]==s2[p2]):
                    p2+=1
                    p4+=1
                ans=ans or check(p1c,p2,p4,[val[0],val[1]+1])
                return ans
            if s3[f]==s1[p1]:
                while(f<tot and p1<m and s3[f]==s1[p1]):
                    p1+=1
                    f+=1
                return check(p1,p2,f,[val[0]+1,val[1]])
            if s3[f]==s2[p2]:
                while(f<tot and p2<n and s3[f]==s2[p2]):
                    p2+=1
                    f+=1
                return check(p1,p2,f,[val[0],val[1]+1])
            return False
        return check(0,0,0,[0,0])
''' 