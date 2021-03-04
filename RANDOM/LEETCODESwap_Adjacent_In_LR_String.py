#attempt3:TOOK HELP: check if the strings have equal L's and R's and then
#check if the Ls in the start string are to the atmost same level or lesser than
#end string and similarly for R's check if R's can be pushed to the right
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace("X","")!=end.replace("X",""):
            return False
        n=len(start)
        lefts1=[i for i in range(n) if start[i]=='L']
        lefts2=[i for i in range(n) if end[i]=='L']
        rights1=[i for i in range(n) if start[i]=='R']
        rights2=[i for i in range(n) if end[i]=='R']
        for i in range(len(lefts1)):
            if lefts2[i]>lefts1[i]:
                return False
        for i in range(len(rights1)):
            if rights2[i]<rights1[i]:
                return False
        return True

#attempt2 and 1: My attempts
'''
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start=list(start)
        end=list(end)
        n=len(end)-1
        l1,r1,x1=start.count('L'),start.count('R'),start.count('X')
        l2,r2,x2=end.count('L'),end.count('R'),end.count('X')
        if l1==l2 and r1==r2 and x1==x2:
            while(n>-1):
                #print(n)
                if n==0:
                    return start==end
                if start[n]!=end[n]:
                    if start[n]=='X' and end[n]=='R' and start[n-1]=='R' and end[n-1]=='X':
                        start[n]='R'
                        start[n-1]='X'
                        n-=2
                    elif start[n]=='L' and end[n]=='X' and start[n-1]=='X' and end[n-1]=='L':
                        start[n-1]='L'
                        start[n]='X'
                        n-=2
                    elif start[n]=='L' and start[n-1]=='X':
                        start[n-1]='L'
                        start[n]='X'
                        n-=1
                    elif start[n-1]=='R' and start[n]=='X':
                        start[n]='R'
                        start[n-1]='X'
                        n-=1
                    else:
                        return False
                else:
                    n-=1

            return True
        return False
'''
