#attempt6:AC
from heapq import heapify, heappush, heappop
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sumy=sum(target)
        target=[-i for i in target]
        n=len(target)
        heapify(target)
        arr=[-1]*n
        if target==arr:
            return True
        while(True):
            if sumy<n:
                return False
            ele=-heappop(target)
            roe=sumy-ele
            if roe==1:
                return True
            sumy-=ele
            if ele-roe<=0 or roe==0 or ele%roe==0:
                return False
            ele=ele%roe
            heappush(target,-ele)
            if target==arr:
                return True
            sumy+=ele

#attempt5:RunTime Error as whenever we are using % check for denominator first
'''
from heapq import heapify, heappush, heappop
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sumy=sum(target)
        target=[-i for i in target]
        n=len(target)
        heapify(target)
        arr=[-1]*n
        if target==arr:
            return True
        while(True):
            if sumy<n:
                return False
            ele=-heappop(target)
            roe=sumy-ele
            if roe==1:
                return True
            sumy-=ele
            if ele-roe<=0:
                return False
            ele=ele%roe
            heappush(target,-ele)
            if target==arr:
                return True
            sumy+=ele
'''

#attempt4: TLE for [1,1,1,2]
#causes problems as I had removed condition checking if any number in target
#is <=0
'''
from heapq import heapify, heappush, heappop
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sumy=sum(target)
        target=[-i for i in target]
        n=len(target)
        heapify(target)
        arr=[-1]*n
        if target==arr:
            return True
        while(True):
            if sumy<n:
                return False
            ele=-heappop(target)
            roe=sumy-ele
            if roe==1:
                return True
            sumy-=ele
            ele=ele%roe
            heappush(target,-ele)
            if target==arr:
                return True
            sumy+=ele
'''

#attempt3: TLE same mistake as previous
#Problematic because didn't use %
'''
from heapq import heapify, heappush, heappop
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sumy=sum(target)
        target=[-i for i in target]
        n=len(target)
        heapify(target)
        arr=[-1]*n
        if target==arr:
            return True
        while(True):
            if sumy<n:
                return False
            ele=-heappop(target)
            roe=sumy-ele
            if roe==1:
                return True
            sumy-=ele
            ele=ele-roe
            if -ele>0:
                return False
            heappush(target,-ele)
            if target==arr:
                return True
            sumy+=ele
'''

#attempt2:TLE for [1,10000000000]
#**for such cases when subtracting 'by' is very small compared to
#subtracting 'from' use MODULUS**
#Also if ROE is 1 the other number can be converted to 1 and hence return True
'''
from heapq import heapify, heappush, heappop
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sumy=sum(target)
        target=[-i for i in target]
        n=len(target)
        heapify(target)
        arr=[-1]*n
        while(True):
            if target==arr:
                return True
            if sumy<n:
                return False
            ele=-heappop(target)
            roe=sumy-ele
            sumy-=ele
            ele=ele-roe
            if -ele>0:
                return False
            heappush(target,-ele)
            if target==arr:
                return True
            sumy+=ele
'''

#attempt1: TLE

#**It is always easy to go from the given final destination to the initial location**
#IDEA:TOOK HINT
#choose the largest current element and remove it based on other elements
#TLE for [9,9,9]. If (removed element)-(rest of elements)<=0, cant be used
'''
from heapq import heapify, heappush, heappop
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sumy=sum(target)
        target=[-i for i in target]
        n=len(target)
        heapify(target)
        arr=[-1]*n
        while(True):
            if target==arr:
                return True
            if sumy<n:
                return False
            ele=-heappop(target)
            roe=sumy-ele
            sumy-=ele
            ele=ele-roe
            heappush(target,-ele)
            if target==arr:
                return True
            sumy+=ele
        
        
'''
