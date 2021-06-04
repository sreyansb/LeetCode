#attempt3:BFS Very easy
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        queue=deque()
        visited=set()
        for i  in deadends:
            visited.add(i)
        queue.append(("0000",0))
        visited.add('0000')
        while(queue):
            curstr,paths=queue.popleft()
            if curstr==target:
                return paths
            cur=list(curstr)
            for i in range(4):
                temp=cur[i]
                
                if temp=='0':
                    allowed=['9','1']
                elif temp=='9':
                    allowed=['0','8']
                else:
                    nu=int(temp)
                    allowed=[str(nu-1),str(nu+1)]
                
                cur[i]=allowed[0]
                k="".join(cur)
                if k not in visited:
                    queue.append((k,paths+1))
                    visited.add(k)
                
                cur[i]=allowed[-1]
                k="".join(cur)
                if k not in visited:
                    queue.append((k,paths+1))
                    visited.add(k)
                
                cur[i]=temp
        return -1        

#attempt2:WA IDK
'''
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        initial=list('0000')
        dpt={}
        dpt[target]=0
        for i in deadends:
            dpt[i]=float('inf')
        target=list(target)
        
        def dp(initial):
            if initial==target:
                return 0
            k="".join(initial)
            if k in dpt:
                return dpt[k]
            dpt[k]=float('inf')
            for i in range(4):
                temp=initial[i]
                if temp=="0":
                    allowed=["9","0","1"]
                elif temp=="9":
                    allowed=["8","9","0"]
                else:
                    nu=int(temp)
                    allowed=[str(nu-1),temp,str(nu+1)]
                initial[i]=allowed[0]
                dpt[k]=min(dpt[k],1+dp(initial))
                initial[i]=allowed[2]
                dpt[k]=min(dpt[k],1+dp(initial))
                initial[i]=allowed[1]
                dpt[k]=min(dpt[k],dp(initial))
            return dpt[k]
                
        dp(initial)
        k="0000"
        print(dpt)
        return dpt[k] if dpt[k]!=float('inf') else -1
        
'''

#attempt1:TLE also it doesn't depend on index number because you can change them anytime
#Had a wrong idea of the problem, we can move an index to i+1 or i-1 or i
'''
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=[list(i) for i in deadends]
        initial=list('0000')
        dpt={}
        dpt[target]=0
        target=list(target)
        def dp(index,initial):
            if initial==target:
                return 0
            if index>=4 or initial in deadends:
                #print(index,initial)
                return float('inf')
            k="".join(initial)
            if k in dpt:
                return dpt[k]
            temp=initial[index]
            ans=float('inf')
            for i in "0123456789":
                initial[index]=i
                if i!=temp:
                    ans=min(ans,1+dp(index+1,initial))
                else:
                    ans=min(ans,dp(index+1,initial))
            initial[index]=temp
            dpt[k]=ans
            return dpt[k]
        dp(0,initial)
        k="0000"
        #print(dpt)
        return dpt[k] if dpt[k]!=float('inf') else -1
'''