#attempt1:
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        init=1
        index=0
        while(k and index<len(arr)):
            if init!=arr[index]:
                k-=1
                init+=1
                continue
            init+=1  
            index+=1
        if k:
            init=init+k
        return init-1
        
            
        
