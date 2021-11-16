#attempt2: TOOK HELP
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        #if for given element there are enough values
        def enough_elements_less_than(elem_to_check):
            c = 0
            for i in range(1,m+1):
                c += min(elem_to_check//i,n)
            #print(elem_to_check,c)
            return True if c>=k else False
        
        low = 1
        high = m*n
        while(low<high):
            mid = (low+high)//2
            #print(low,high,mid)
            if enough_elements_less_than(mid):
                #print("HERE",lo,high,mid)
                high = mid
            else:
                low = mid+1
                #print("HERE",low,high,mid)
        return low
                
            

#attempt1:TLE Brute Force
'''
from heapq import heappush,heappop
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        alls = []
        for i in range(1,m+1):
            for j in range(1,n+1):
                heappush(alls,i*j)
        ele = -1
        while(k):
            ele = heappop(alls)
            k -= 1
        return ele
'''
