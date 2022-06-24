#attempt2: COPIED : Almost 0 form
from heapq import heapify, heappush, heappop
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sumy=sum(target)
        target=[-i for i in target]
        n=len(target)
        heapify(target)
        if set(target)=={-1}:
            return True
        while(True):
            if set(target)=={-1}:
                return True
            highest=-heappop(target)
            roe=sumy-highest
            sumy-=highest
            if roe==1:
                return True
            if roe==0 or highest%roe==0 or highest<=roe:
                return False
            sumy+=(highest%roe)
            heappush(target,-(highest%roe))
        
        
        

#attempt1: TLE
'''
from heapq import heappush,heappop
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        totalsum = 0
        max_heap = []
        for i in target:
            heappush(max_heap,-i)
            totalsum += i
        while(True):
            maxele = -heappop(max_heap)
            if maxele == 1:
                break
            sum_without_max = totalsum - maxele
            if maxele-sum_without_max >= 1:
                heappush(max_heap,-maxele+sum_without_max)
                totalsum = maxele
            else:
                return False
            #print(max_heap)
        return True
        
        
'''
