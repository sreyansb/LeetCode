#attempt2:Used suffix sum for sols
from bisect import bisect_right
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        di={}
        dil={}
        
        for i in t:
            di[i]=[]
            dil[i]=0
        
        for i in range(len(s)):
            if s[i] in di:
                di[s[i]].append(i)
                dil[s[i]]+=1
        
        sols={}
        for i in t:
            sols[i]=[1 for i in range(dil[i])]
        for i in range(dil[t[-1]]-2,-1,-1):
            sols[t[-1]][i]+=sols[t[-1]][i+1]
        #print(di)
        for i in range(len(t)-2,-1,-1):
            character=t[i]
            for sindex in range(dil[character]):
                pos=bisect_right(di[t[i+1]],di[character][sindex])
                if pos==dil[t[i+1]]:
                    sols[character][sindex]=0
                else:
                    sols[character][sindex]=sols[t[i+1]][pos]
            for sindex in range(dil[character]-2,-1,-1):
                sols[character][sindex]+=sols[character][sindex+1]
            #print(sols)
        if sols[t[0]]:
            return (sols[t[0]][0])
        return 0

#attempt1: TLE : all test cases passed but didn't accept the soln
'''
from bisect import bisect_right
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        di={}
        dil={}
        
        for i in t:
            di[i]=[]
            dil[i]=0
        
        for i in range(len(s)):
            if s[i] in di:
                di[s[i]].append(i)
                dil[s[i]]+=1
        
        sols={}
        for i in t:
            sols[i]=[1 for i in range(dil[i])]
        #print(di)
        for i in range(len(t)-2,-1,-1):
            character=t[i]
            for sindex in range(dil[character]):
                pos=bisect_right(di[t[i+1]],di[character][sindex])
                if pos==dil[t[i+1]]:
                    sols[character][sindex]=0
                else:
                    sols[character][sindex]=sum(sols[t[i+1]][pos:])
            #print(sols)
        return sum(sols[t[0]])
'''