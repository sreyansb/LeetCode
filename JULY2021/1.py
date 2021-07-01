#attempt2: Faster but still slow
class Solution:
    def grayCode(self, n: int) -> List[int]:
        reqd=1<<n
        visited={0:1}
        ans=[0]
        def dfs(curele,visited,curlen):
            if curlen==reqd:
                ans[0]=[i for i in visited.keys()]
                return
            if ans[0]:
                return
            for i in range(n):
                newele=curele^(1<<i)
                if newele not in visited:
                    visited[newele]=1
                    dfs(newele,visited,curlen+1)
                    del visited[newele]
        dfs(0,visited,1)
        return ans[0]

#Attempt1: Faster lookup and also ordered insertion ke liye I have used dictionary.
#Planned to use only list but slow. Planned to use set but not ordered
'''
class Solution:
    def grayCode(self, n: int) -> List[int]:
        reqd=1<<n
        finalans=[0]
        def dfs(curword,visited,leng):
            if leng==reqd:
                finalans[0]=["".join(i) for i in visited.keys()]
                return
            if finalans[0]:
                return
            for i in range(n):
                temp=curword[i]
                curword[i]="0" if temp=="1" else "1"
                new="".join(curword)
                if new not in visited:
                    visited[new]=1
                    dfs(curword,visited,leng+1)
                    del visited[new]
                curword[i]=temp
        dfs(["0"]*n,{"0"*n:1},1)
        finalans[0]=[int(i,2) for i in finalans[0] ]
        return finalans[0]
'''