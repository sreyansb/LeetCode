#attempt1:
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        if n<3:
            return False
        index=1
        downstart,upstart=0,0
        while(index<n):
            if not(downstart):
                if arr[index]>arr[index-1]:
                    upstart=1
                    index+=1
                    continue
                elif arr[index]==arr[index-1]:
                    return False
                else:
                    downstart=1
            else:
                if arr[index]<arr[index-1]:
                    index+=1
                    continue
                else:
                    return False
        return True if (downstart and upstart) else False
        
