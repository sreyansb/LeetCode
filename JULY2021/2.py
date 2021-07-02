#attempt2: dont put in ans array. Just keep start and end and answer is from start+1 uptil end-1
from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos=bisect_left(arr,x)
        start=pos-1
        end=pos
        n=len(arr)
        ans=[]
        while(k and start>-1 and end<n):
            diffl=x-arr[start]
            diffr=arr[end]-x
            if diffr<diffl:
                
                end+=1
            else:
                
                start-=1
            k-=1
            #print(start,end,ans)
        while(k and start>-1):
            
            start-=1
            k-=1
        while(k and end<n):
            
            end+=1
            k-=1
        return arr[start+1:end]

#attempt1: speed is less and storage is high
'''
from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos=bisect_left(arr,x)
        start=pos-1
        end=pos
        n=len(arr)
        ans=[]
        while(k and start>-1 and end<n):
            diffl=x-arr[start]
            diffr=arr[end]-x
            if diffr<diffl:
                ans.append(arr[end])
                end+=1
            else:
                ans.append(arr[start])
                start-=1
            k-=1
            #print(start,end,ans)
        while(k and start>-1):
            ans.append(arr[start])
            start-=1
            k-=1
        while(k and end<n):
            ans.append(arr[end])
            end+=1
            k-=1
        return sorted(ans)
'''