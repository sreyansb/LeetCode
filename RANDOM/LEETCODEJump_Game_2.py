#attempt2: 5%
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        m=float('inf')
        n=len(nums)
        goods=[float('inf') for i in range(n)]
        goods[-1]=0
        for i in range(n-2,-1,-1):
            if i+nums[i]>=n-1:
                goods[i]=1
            else:
                if nums[i]==0:
                    continue
                k=min(goods[i+1:i+nums[i]+1])
                goods[i]=k+1
        #print(goods)
        return goods[0]
'''
#attempt1:TLE
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        m=float('inf')
        n=len(nums)
        goods=[float('inf') for i in range(n)]
        goods[-1]=0
        for i in range(n-2,-1,-1):
            if i+nums[i]>=n-1:
                goods[i]=1
            else:
                for j in range(i+nums[i],i,-1):
                    goods[i]=min(goods[i],goods[j]+1)
        #print(goods)
        return goods[0]
'''
                    
                    
