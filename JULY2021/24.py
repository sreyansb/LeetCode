#attempt6:TOOK HELP AC used BFS to find minimum steps to reach endWord and kept a distance array
#To find distance between beginWord and currentword. THen perform DFS(with Pruning)
#remember child node values can be equal to distance[endWord]
#also we make a graph to find all words a word can reach
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        wordList=set(wordList)
        graph={}
        wordList.add(beginWord)
        n,k=len(wordList),len(endWord)
        for i in wordList:
            if i not in graph:
                graph[i]=set() #very important if no path from A to B 
            for j in range(k):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    newword=i[:j]+char+i[j+1:]
                    if char!=i[j] and newword in wordList:
                        if newword not in graph:
                            graph[newword]=set()
                        graph[i].add(newword)
                        graph[newword].add(i)
        dist={}
        queue=deque([])
        queue.append((beginWord,1))
        visited={beginWord}
        while(queue):
            curnode,d=queue.popleft()
            dist[curnode]=d
            for child in graph[curnode]:
                if child not in visited:
                    queue.append((child,d+1))
                    visited.add(child)
        #print(dist)
        #return
        ans=[]
        stack=[[beginWord]]
        while(stack):
            curpath=stack.pop()
            if curpath[-1]==endWord:
                #print("here")
                if dist[endWord]==len(curpath):
                    ans.append(curpath.copy())
                continue
            for child in graph[curpath[-1]]:
                if (dist[curpath[-1]]<dist[child]<=dist[endWord]):
                    stack.append((curpath+[child]).copy())
        
        return ans

#attempt4: Changed many things but still TLE
'''
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        wordList=set(wordList)
        n=len(endWord)
        queue=deque([])
        queue.append((beginWord,[beginWord]))
        ans=[]#word with list
        minl=[float('inf')]
        while(queue):
            word,curlist=queue.popleft()
            #print(word)
            leng=len(curlist)
            if word==endWord:
                if leng>minl[0]:
                    continue
                minl[0]=min(minl[0],leng)
                ans.append(curlist.copy())
                continue
            if len(curlist)>=minl[0]:
                continue
            word=list(word)
            for i in range(n):
                temp=word[i]
                for char in "qwertyuiopasdfghjklzxcvbnm":
                    if char==temp:
                        continue
                    word[i]=char
                    k="".join(word)
                    if k in wordList and k not in curlist:
                        queue.append((k,curlist+[k]))
                word[i]=temp
        if not(ans):
            return []
        ans.sort(key=len)
        fians=[]
        for i in range(1,len(ans)+1):
            if len(ans[i-1])!=minl[0]:
                return ans[:i]
        return ans
'''

#attempt3: TLE still continued with BFS and tried to improve the code 
'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        wordList=set(wordList)
        n=len(endWord)
        ans=[]
        di={}
        for i in range(n):
            di[i]=set()
        for i in wordList:
            for j in range(n):
                di[j].add(i[j])
        
        minl=[float('inf')]
        def recurse(word,current,curlen,currentset):
            if word==endWord:
                #print(curlen)
                minl[0]=min(minl[0],curlen)
                ans.append(current.copy())
                return
            if curlen>=minl[0]:
                return
            word=list(word)
            for i in range(n):
                temp=word[i]
                for j in di[i]:
                    word[i]=j
                    k="".join(word)
                    if k in wordList and k not in currentset:
                        recurse(k,current+[k],curlen+1,currentset|{k})
                word[i]=temp
        recurse(beginWord,[beginWord],1,{beginWord})
        ans=sorted(ans,key=len)
        if not(ans):
            return []
        k=minl[0]
        #print(ans)
        finans=[]
        for i in ans:
            #print(i)
            if len(i)!=k:
                break
            finans.append(i)
        return finans
'''

#attempt2: TLE: attempted bfs. TLE because we cant prune stuff in bfs as we need to find all answers 
'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        wordList=set(wordList)
        n=len(endWord)
        ans=[]
        def recurse(word,current):
            if word==endWord:
                ans.append(current.copy())
                return
            word=list(word)
            for i in range(n):
                temp=word[i]
                for j in "qwertyuiopasdfghjklzxcvbnm":
                    word[i]=j
                    k="".join(word)
                    if k in wordList and k not in current:
                        recurse(k,current+[k])
                word[i]=temp
        recurse(beginWord,[beginWord])
        ans=sorted(ans,key=len)
        if not(ans):
            return []
        k=len(ans[0])
        #print(ans)
        finans=[]
        for i in ans:
            #print(i)
            if len(i)!=k:
                break
            finans.append(i)
        return finans
'''

#Attempt 1 and 5: Runtime error: problem because I didn't take into consideration 0 paths from begin to end
'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        wordList=set(wordList)
        n=len(endWord)
        ans=[]
        def recurse(word,current):
            if word==endWord:
                ans.append(current.copy())
                return
            word=list(word)
            for i in range(n):
                temp=word[i]
                for j in "qwertyuiopasdfghjklzxcvbnm":
                    word[i]=j
                    k="".join(word)
                    if k in wordList and k not in current:
                        recurse(k,current+[k])
                word[i]=temp
        recurse(beginWord,[beginWord])
        ans=sorted(ans,key=len)
        k=len(ans[0])
        #print(ans)
        finans=[]
        for i in ans:
            #print(i)
            if len(i)!=k:
                break
            finans.append(i)
        return finans
'''