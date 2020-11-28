#attempt5: 70%
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        n=len(nums)
        queue=deque([])
        for i in range(k):
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
            queue.append(i)
        for i in range(k,n):
            ans.append(nums[queue[0]])
            while queue and queue[0]<=i-k:
                queue.popleft()
            while(queue and nums[queue[-1]]<nums[i]):
                queue.pop()
            queue.append(i)
        ans.append(nums[queue[0]])
        return ans
            

#attempt4:35%  AC -> check book took help->GFG -> quite a problem
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        n=len(nums)
        queue=[]
        for i in range(k):
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
            queue.append(i)
        for i in range(k,n):
            ans.append(nums[queue[0]])
            while queue and queue[0]<=i-k:
                queue.pop(0)
            while(queue and nums[queue[-1]]<nums[i]):
                queue.pop()
            queue.append(i)
        ans.append(nums[queue[0]])
        return ans
'''

#attempt3: TLE 50
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        n=len(nums)
        di={}
        for i in range(k):
            if nums[i] not in di:
                di[nums[i]]=0
            di[nums[i]]+=1
        ans.append(max(di))
        for i in range(k,n):
            di[nums[i-k]]-=1
            if di[nums[i-k]]==0:
                di.pop(nums[i-k])
            if nums[i] not in di:
                di[nums[i]]=0
            di[nums[i]]+=1
            ans.append(max(di))
        return ans
'''

#attempt2:WA and TLE
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        n=len(nums)
        window=set(nums[:k])
        ans.append(max(window))
        for i in range(k,n):
            window=window-{nums[i-k]}
            window=window|{nums[i]}
            ans.append(max(window))
        return ans
'''
#attempt1: TLE 49/59
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        window=nums[:k-1]
        for i in nums[k-1:]:
            window.append(i)
            ans.append(max(window))
            window=window[1:]
        return ans
        
'''
