#attempt3: TOOK HINT
#have to make dp tables such that it captures the location of the 
#closest left,top,right and bottom zeroes. Template program based on another
#problem. 
#The answer at a particular index is min of the dp tables
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        ans=0
        mines=set(tuple(i) for i in mines)
        left=[[0 for i in range(n+2)]for j in range(n+2)]
        top=[[0 for i in range(n+2)]for j in range(n+2)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if (i-1,j-1) in mines:
                    left[i][j]=0
                    top[i][j]=0
                else:
                    left[i][j]=left[i-1][j]+1
                    top[i][j]=top[i][j-1]+1
        for i in range(n,0,-1):
            for j in range(n,0,-1):
                if (i-1,j-1) in mines:
                    left[i][j]=0
                    top[i][j]=0
                else:
                    left[i][j]=min(left[i+1][j]+1,left[i][j])
                    top[i][j]=min(top[i][j+1]+1,top[i][j])
                ans=max(ans,min(left[i][j],top[i][j]))
        return ans

#attempt2: TLE even though I made it a set
'''
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        ans=0
        mines=set(tuple(i) for i in mines)
        def check(r,c):
            r1,r2=r,r
            c1,c2=c,c
            ans=0
            while(r1>-1 and r2<n and c1>-1 and c2<n and (r1,c) not in mines and (r2,c) not in mines and (r,c1) not in mines and (r,c2) not in mines):
                ans+=1
                r1-=1
                r2+=1
                c1-=1
                c2+=1
            return ans
        for i in range(n):
            for j in range(n):
                if (i,j) not in mines:
                    ans=max(ans,check(i,j))
        return ans
'''

#attempt1: TLE because like an idiot I didn't make mines a set.
'''
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        ans=0
        mines=[tuple(i) for i in mines]
        def check(r,c):
            r1,r2=r,r
            c1,c2=c,c
            ans=0
            while(r1>-1 and r2<n and c1>-1 and c2<n and (r1,c) not in mines and (r2,c) not in mines and (r,c1) not in mines and (r,c2) not in mines):
                ans+=1
                r1-=1
                r2+=1
                c1-=1
                c2+=1
            return ans
        for i in range(n):
            for j in range(n):
                if (i,j) not in mines:
                    ans=max(ans,check(i,j))
        return ans
'''