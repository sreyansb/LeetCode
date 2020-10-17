#attempt3: AC - quite an easy solution
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        di={}
        n=len(s)
        index=0
        ans=set()
        while(index<=n-10):
            k=s[index:index+10]
            if k not in di:
                di[k]=0
            di[k]+=1
            if di[k]>1:
                ans.add(k)
            index+=1
        return list(ans)

#attempt2: TLE 25/32
"""
import re
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        di=set()
        #print(s,s.count("AAAAAAAAAA"))
        k="ATGC"
        for a in k:
            for b in k:
                for c in k:
                    for d in k:
                        for e in k:
                            for f in k:
                                for g in k:
                                    for h in k:
                                        for i in k:
                                            for j in k:
                                                l=a+b+c+d+e+f+g+h+i+j
                                                index=s.find(l)
                                                if index!=-1:
                                                    index1=s.find(l,index+1)
                                                    if index1!=-1:
                                                        di.add(l)
        return list(di)
"""                                               
        

#attempt1: TLE 31/32 as expected TLE
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        index=0
        n=len(s)
        ans=[]
        di=set()
        while(index<=n-10):
            k=s[index:index+10]
            if k not in di:
                if s.find(k,index+1)!=-1:
                    ans+=[k]
                di.add(k)
            index+=1
        return ans
"""       
