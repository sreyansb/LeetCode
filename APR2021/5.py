#attempt5:
'''
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        n=len(A)
        heap=[]
        mini=A[-1]
        for i in range(n-3,-1,-1):
            if A[i]>mini:
                return False
            mini=min(mini,A[i+1])
        return True
'''

#attempt4: minimum
'''
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        n=len(A)
        heap=[]
        mini=A[-1]
        for i in range(n-3,-1,-1):
            if mini<A[i]:
                return False
            mini=min(mini,A[i+1])
        return True
'''

#attempt3: HEAP
'''
from heapq import heappush
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        n=len(A)
        heap=[]
        heappush(heap,A[-1])
        for i in range(n-3,-1,-1):
            if heap[0]<A[i]:
                return False
            heappush(heap,A[i+1])
        return True
'''

#attempt2:Used heap from back -> and also problem was i should be from n-3
'''
from heapq import heappush
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        n=len(A)
        heap=[]
        heappush(heap,A[-1])
        for i in range(n-2,-1,-1):
            if heap[0]<A[i]:
                return False
            heappush(heap,A[i+1])
        return True
'''

#attempt1: TLE
'''
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        n=len(A)
        lo=0
        gl=0
        for i in range(n-2):
            for j in range(i+2,n):
                if A[i]>A[j]:
                    return False
        return True
'''
