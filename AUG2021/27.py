#Attempt3: Probably the worst wordd question: USED regex
#we need to find the length of the word which doesn't appear in other words as a 
#subsequence(if even one character doesn't appear in other subsequences/ order is different)
#-> that the entire word doesn't appear
import re
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        n=len(strs)
        finans=-1
        strs.sort(key=len,reverse=True)
        for i in range(n):
            newregex=""
            for ch in strs[i]:
                newregex=newregex+".*"+ch# . is very important
            newregex+=".*"
            flag=1
            for j in range(n):
                if j==i:
                    continue
                if re.match(newregex,strs[j]):
                    flag=0
                    break
            if flag:
                return len(strs[i])
        return -1

#attempt2: INCOMPLETE Attempted to use LCS logic for LUS, wrong implementation
#because LUS is a subsequence of string 1 which is not a subsequence of 2
#i.e. if len(word1)!=len(word2): return the max len
#else if a==b return -1 else return len(a)
'''
#find LUS between pair of words and use this LUS string as the string for the next one
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        n=len(strs)
        if n==1:
            return -1
        def findlus(word1,word2):
            m,n=len(word1),len(word2)
            dpt=[[0 for i in range(n+1)] for j in range(m+1)]
            for i in range(m+1):
                for j in range(n+1):
                    if i==0 or j==0:
                        dpt[i][j]=0
                    if word1[i-1]!=word2[j-1]:
                        dpt[i][j]=dpt[i-1][j-1]+1
                    dpt[i][j]=max(dpt[i-1][j],dpt[i][j-1])
            wordi=[""]*dpt[m][n]
            index=dpt[m][n]-1
            i,j=m,n
            while(i>0 and j>0):
                if word1[i]!=word2[j]:
                    wordi[index]=word1[i]
                    index-=1
                    i-=1
                    j-=1
                elif dpt[i-1][j]>dpt[i][j-1]:
                    i-=1
                else:
                    j-=1
            wordj=[""]*dpt[m][n]
            index=dpt[m][n]-1
            i,j=m,n
            while(i>0 and j>0):
                if word1[i]!=word2[j]:
                    wordj[index]=word2[j]
                    index-=1
                    i-=1
                    j-=1
                elif dpt[i-1][j]>dpt[i][j-1]:
                    i-=1
                else:
                    j-=1
            return ["".join(wordi),"".join(wordj)]
        v1,v2=findlus(strs[0],strs[1])
        def recurse(index,v1,v2):
            if index>=n:
                return
            v1,v2=findlus(strs[index],v1),findlus(strs[index],v2)
            ans1=recurse(index+1,v1,v2)
'''

#attempt1: I found intersection of all strings completely dumb stuff
'''
#find an intersection between all words
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        finaldi={}
        for i in strs[0]:
            if i not in finaldi:
                finaldi[i]=0
            finaldi[i]+=1
        for i in strs[1:]:
            curdi={}
            for j in i:
                if j not in curdi:
                    curdi[j]=0
                curdi[j]+=1
            for ch in curdi:
                if ch not in finaldi:
                    continue
                finaldi[ch]=min(finaldi[ch],curdi[ch])
            charstobedeleted=[]
            for ch in finaldi:
                if ch not in curdi:
                    charstobedeleted.append(ch)
            for i in charstobedeleted:
                del finaldi[i]
        ans=0
        for i in finaldi:
            ans+=finaldi[i]
        return ans if ans else -1
'''