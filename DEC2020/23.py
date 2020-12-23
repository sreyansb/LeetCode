#attempt2:AC after many attempts had to seee INT_MAX value
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        k=list(str(n))
        if sorted(k,reverse=True)==k or n>=2**32:
            return -1
        leng=len(k)
        index=-1
        for i in range(leng-1,0,-1):
            if k[i]>k[i-1]:
                index=i
                break
        for i in range(leng-1,index-1,-1):
            if k[index-1]<k[i]:
                k[index-1],k[i]=k[i],k[index-1]
                k=k[:index]+k[index:][::-1]
                k=int("".join(k))
                return k if k<2**31 else -1
                
        
        

#attempt1: WA -> because didnt read the problem properly
#len(k)>32 is wrong  n<2**32 is right
'''
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        k=list(str(n))
        if sorted(k,reverse=True)==k or len(k)>32:
            return -1
        leng=len(k)
        index=-1
        for i in range(leng-1,0,-1):
            if k[i]>k[i-1]:
                index=i
                break
        for i in range(leng-1,index-1,-1):
            if k[index-1]<k[i]:
                k[index-1],k[i]=k[i],k[index-1]
                k=k[:index]+k[index:][::-1]
                return int("".join(k))
'''     
        
