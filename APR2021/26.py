#attempt2:
from heapq import heappush,heappop
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        n=len(heights)
        cursum=0
        for i in range(1,n):
            diff=heights[i]-heights[i-1]
            if diff>0:
                heappush(heap,-diff)
                cursum+=diff
                if cursum>bricks:
                    if ladders==0:
                        return i-1
                    ladders-=1
                    maxi=heappop(heap)*-1
                    cursum-=maxi
        return n-1
        

#attempt1: Used the clues WA Fails for 1 5 1 2 3 4 1000 with 1 rope and 4 bricks
''' 
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n=len(heights)
        diff=[]
        for i in range(1,n):
            diff.append(heights[i]-heights[i-1])
        maxdiff=sorted(diff,reverse=True)[:ladders]
        di={}
        for i in maxdiff:
            if i not in di:
                di[i]=0
            di[i]+=1
        cursum=0
        #print(diff)
        for i in range(1,n):
            if diff[i-1]<=0:
                continue
            k=diff[i-1]
            #print(k,cursum,di)
            if k in di:
                di[k]-=1
                if di[k]==0:
                    del di[k]
            else:
                if cursum+k<=bricks:
                    cursum+=k
                else:
                    flag=0
                    for i in di:
                        flag=1
                        di[i]-=1
                        if di[i]==0:
                            del di[i]
                        break
                    if flag==0:
                        #print("i",i,k,cursum,di)
                        return i-1
        return n-1
'''
