#attempt1:
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        '''
        di = {}
        ans = 0
        for j in range(len(nums)):
            if nums[j]-k in di:
                ans += di[nums[j]-k]
            if nums[j]+k in di:
                ans += di[nums[j]+k]
            if nums[j] not in di:
                di[nums[j]] = set()
            di[nums[j]] += 1
        return ans
        '''
        if k==0:
            ans = 0
            di = {}
            for i in nums:
                if i not in di:
                    di[i] = 0
                di[i] += 1
            for i in di:
                if di[i]>1:
                    ans += 1
            return ans
                
        nums = list(set(nums))
        ans = 0
        di = {}
        for j in range(len(nums)):
            if nums[j]-k in di:
                ans += di[nums[j]-k]
            if nums[j]+k in di:
                ans += di[nums[j]+k]
            if nums[j] not in di:
                di[nums[j]] = 0
            di[nums[j]] += 1
        return ans
        
