#attempt1:
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        fronty=[nums[0]]
        endy=[nums[-1]]
        if len(nums)==1:
            return 1 if nums[0]==x else -1
        for i in range(1,len(nums)):
            fronty.append(fronty[-1]+nums[i])
        for i in range(len(nums)-2,-1,-1):
            endy.append(endy[-1]+nums[i])
        mini=float('inf')
        if x in fronty:
            mini=min(mini,fronty.index(x)+1)
        if x in endy:
            mini=min(mini,endy.index(x)+1)
        front={n:i for i,n in enumerate(fronty)}
        end={n:i for i,n in enumerate(endy)}
        for i in front:
            if i>x:
                break
            if x-i in end:
                mini=min(mini,front[i]+2+end[x-i])
        return mini if (mini!=float('inf') and sum(nums)>=x) else -1
    #the condition sum(nums)>=x is very important
            
            
        
