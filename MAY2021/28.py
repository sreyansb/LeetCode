from collections import deque
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxie=-float('inf')
        n=len(nums)
        queue=deque([])
        elewin={} #for quick lookups
        summy=0
        for i in range(n):
            if nums[i] in elewin:
                while(queue and queue[0]!=nums[i]):
                    ele=queue.popleft()
                    del elewin[ele]
                    summy-=ele
                if queue:
                    queue.popleft()
                    summy-=nums[i]
            queue.append(nums[i])
            elewin[nums[i]]=0
            summy+=nums[i]
            maxie=max(maxie,summy)
            #print(queue)
        return maxie
                
            
            
        