#attempt4: AC
from collections import deque
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        queue = deque([])
        maxl = max(nums)
        hasneg = [0 for i in range(n)]
        #haszero = [0 for i in range(n)]
        for i in range(n-2,-1,-1):
            if nums[i+1]<0:
                hasneg[i] = 1
            else:
                hasneg[i] = 1+hasneg[i+1]
            
        curpdt = 1
        for i in range(n):
            prevcrud = curpdt
            curpdt *= nums[i]
            queue.append(nums[i])
            maxl = max(maxl,curpdt)
            if curpdt<0:
                if hasneg[i]:
                    continue
                while(queue and curpdt<0):
                    curpdt //= queue.popleft()
                if queue:
                    maxl = max(maxl,curpdt)
            elif curpdt==0:
                while(queue[0]!=0):
                    maxl = max(maxl,prevcrud)
                    prevcrud //= queue.popleft()
                    
                curpdt = 1
                queue = deque([])
                
            
        return maxl
            
#attempt3: WA because didnt take care of 0 coming before negative coming
'''
from collections import deque
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        queue = deque([])
        maxl = max(nums)
        hasneg = [0 for i in range(n)]
        for i in range(n-2,-1,-1):
            if nums[i+1]<0:
                hasneg[i] = 1
            else:
                hasneg[i] = hasneg[i+1]
        curpdt = 1
        for i in range(n):
            curpdt *= nums[i]
            queue.append(nums[i])
            maxl = max(maxl,curpdt)
            if curpdt<0:
                if hasneg[i]:
                    continue
                while(queue and curpdt<0):
                    curpdt //= queue.popleft()
                if queue:
                    maxl = max(maxl,curpdt)
            elif curpdt==0:
                curpdt = 1
                queue = deque([])
                
            
        return maxl
'''

#attempt2: WA didnt handle negatives properly
'''
from collections import deque
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        queue = deque([])
        maxl = max(nums)
        hasneg = [0 for i in range(n)]
        for i in range(n-2,-1,-1):
            if nums[i+1]<0:
                hasneg[i] = 1
            else:
                hasneg[i] = hasneg[i+1]
        curpdt = 1
        for i in range(n):
            curpdt *= nums[i]
            queue.append(nums[i])
            maxl = max(maxl,curpdt)
            if curpdt<0:
                if hasneg[i]:
                    continue
                while(queue and curpdt<0):
                    curpdt //= queue.popleft()
            elif curpdt==0:
                curpdt = 1
                queue = deque([])
                
            
        return maxl
'''

#attempt1:WA didnt take care of negatives properly
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        hasneg = [0 for i in range(n)]
        
        for i in range(n-2,-1,-1):
            if nums[i+1]<0:
                hasneg[i] = 1
            else:
                hasneg[i] = hasneg[i+1]
            
        maxl = max(nums)
        curpdt = 1
        for i in range(n):
            curpdt *= nums[i]
            if curpdt<0 and hasneg[i]==0:
                curpdt = 1
            elif curpdt==0:
                curpdt = 1
            else:
                maxl = max(maxl,curpdt)
        return maxl
'''
