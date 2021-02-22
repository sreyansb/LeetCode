#attempt2: Very difficult looking question
from bisect import bisect_right
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        #print("jpthiudqzzeugzwwsngebdeai" in d)
        di={}
        n=len(s)
        for i in range(n):
            if s[i] not in di:
                di[s[i]]=[]
            di[s[i]].append(i)
        leng=0
        bestans=""
        for i in d:
            flag=1
            if i[0] not in di:
                continue
            startpos=di[i[0]][0]
            for j in i[1:]:
                    if j not in di:
                        flag=0
                        break
                    pos=bisect_right(di[j],startpos)
                    if pos==len(di[j]):
                        flag=0
                        break
                    startpos=di[j][pos]
                    
            if flag:
                if leng<len(i):
                    leng=len(i)
                    bestans=i
                elif leng==len(i):
                    bestans=min(i,bestans)
        return bestans

#attempt1: TLE 6/31
"""
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d=set(d)
        bestans=[""]
        l=[0]
        nlen=len(s)
        def recurse(index,curstr):
            if curstr in d:
                n=len(curstr)
                if l[0]<n:
                    bestans[0]=curstr
                    l[0]=n
                elif l[0]==n:
                    bestans[0]=min(curstr,bestans[0])
            if index>=nlen:
                return
            recurse(index+1,curstr+s[index])
            recurse(index+1,curstr)
        recurse(0,"")
        return bestans[0]
"""
