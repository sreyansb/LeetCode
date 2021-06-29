#attempt1: Quite a problem this is
from collections import deque
class Solution:
    def longestOnes(self, nums, k: int):
        #window=[]
        zeropos=deque()
        zeroposlen=0
        windowlen=0
        maxans=0
        n=len(nums)
        i=0
        while(i<n):
            if nums[i]:
                #window.append(1)
                i+=1
                windowlen+=1
                maxans=max(maxans,windowlen)
            else:
                if zeroposlen==k:
                    if k==0:
                        #window=[]
                        windowlen=0
                        i+=1
                        continue
                    pos=zeropos.popleft()
                    zeroposlen-=1
                    #window=nums[pos+1:i]
                    windowlen=i-1-pos-1+1
                zeropos.append(i)
                zeroposlen+=1
                windowlen+=1
                maxans=max(maxans,windowlen)
                i+=1                
        return maxans
                    
            
        