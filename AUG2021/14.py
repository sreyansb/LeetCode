#attempt2:TOOK HELP.
#always group same consecutive colours together at the beginning
#We take consecutive same colour boxes and find what ans is possible
#for rest
#Same colour might appear later and hence we do is that find the next position where
#same color as left appears and perform max between prev ans and recurse for 2 halves
from functools import lru_cache
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def recurse(left,right,k):
            if left>=right:
                return 0
            while(left<right-1 and boxes[left]==boxes[left+1]):
                left+=1
                k+=1
            ans=(k+1)*(k+1)+recurse(left+1,right,0)#without same colour appearing again
            for t in range(left+1,right):
                if boxes[t]==boxes[left]:
                    ans=max(ans,recurse(left+1,t,0)+recurse(t,right,k+1))
            return ans
        return recurse(0,len(boxes),0)
        
#attempt1: Used bitmasking
#exponential because visited can take 2^n states and n<=100
'''
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n=len(boxes)
        nset=set(range(n))
        final=(1<<n)-1
        @lru_cache(None)
        def recurse(visited):
            if visited==final:
                return 0
            #print(visited)
            ans=-float('inf')
            index=0
            while(index<n):
                if visited&(1<<index):
                    continue
                index2=index+1#first invalid position
                newvisited=1<<index
                while(index2<n):
                    if visited&(1<<index2):
                        continue
                    if boxes[index2]!=boxes[index]:
                        break
                    newvisited=newvisited|1<<index2
                    index2+=1
                k=index2-1-index+1
                ans=max(ans,(k*k)+recurse(visited|newvisited))
                index=index2
            return ans
        return recurse(0)
'''