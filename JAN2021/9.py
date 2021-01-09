#attempt n+1:USED BFS INStead of DFS
from math import inf
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        
        if endWord not in wordList:
            #print("here")
            return 0
        dp={}
        
        '''
        def checkdifference(curword,i):
            no=0
            if len(curword)!=len(i):
                return False
            for j in range(len(curword)):
                if curword[j]!=i[j]:
                    no+=1
                if no>1:
                    break
            return no==1
        '''
        
        def cal(curword):
            curword=list(curword)
            l=set()
            for i in range(len(curword)):
                a=curword[i]
                for j in range(26):
                    curword[i]=chr(97+j)
                    jw="".join(curword)
                    if (jw in wordList):
                        l.add(jw)
                curword[i]=a
                #print(curword)
            #print(curword,l)
            l=l-{"".join(curword)}
            return l
        
        def dfs(curword):
            #print(curword)
            de=[(curword,1)]
            visited=set()
            while(de):
                newones=[]
                for i in de:
                    visited.add(i[0])
                    for j in cal(i[0]):
                        if j not in visited:
                            newones.append([j,i[1]+1])
                            if j==endWord:
                                return i[1]+1
                de=newones.copy()
                #print(de)
            return 0
                    
        k=dfs(beginWord)
        #print(dp)
        return k if (k!=inf and k!=0) else 0
#attempt n: TLE AND WA-> I still dont know why I got WA for 32nd test case.
#for every time the code was run, I got different answers for 32nd test case.
'''
from math import inf
import sys
sys.setrecursionlimit(10**6)
from math import inf
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList=set(wordList)
        
        if endWord not in wordList:
            #print("here")
            return 0
        dp={}
        
        
        def checkdifference(curword,i):
            no=0
            if len(curword)!=len(i):
                return False
            for j in range(len(curword)):
                if curword[j]!=i[j]:
                    no+=1
                if no>1:
                    break
            return no==1
        
        def cal(curword):
            curword=list(curword)
            l=set()
            for i in range(len(curword)):
                a=curword[i]
                for j in range(26):
                    curword[i]=chr(97+j)
                    jw="".join(curword)
                    if (jw in wordList):
                        l.add(jw)
                curword[i]=a
                #print(curword)
            #print(curword,l)
            l=l-{"".join(curword)}
            return l
        
        def dfs(curword,visited=set(),nofvalues=0):
            #print(curword)
            if curword in visited:
                return inf
            #if curword in dp:
            #   return dp[curword]
            if curword==endWord:
                return nofvalues
            maxie=inf
            visited.add(curword)
            for i in wordList:
                if i not in visited and checkdifference(curword,i):
                    maxie=min(maxie,1+dfs(i,visited,nofvalues))
            visited.remove(curword)
            dp[curword]=maxie
            return maxie
        
        k=dfs(beginWord)
        #print(dp)
        return k+1 if (k!=inf and k!=0) else 0
'''    
        
