#attempt5:
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        frontsum = [0]
        endsum = [0]
        for i in nums:
            frontsum.append(i+frontsum[-1])
        for i in nums[::-1]:
            endsum.append(i+endsum[-1])
        ans = float('inf')
        n = len(frontsum)
        
        #print(frontsum,endsum)
        
        def binsearch(key):
            low = 0
            end = n-1
            while(low<=end):
                mid = (low+end)//2
                if endsum[mid] == key:
                    return mid
                if endsum[mid] > key:
                    end = mid-1
                else:
                    low = mid+1
            return -1
        
        for index in range(n):
            if frontsum[index] <= x:
                endindex = binsearch(x-frontsum[index])
                if endindex != -1 and n-endindex != index:
                    ans = min(ans,index+endindex)
        
        return ans if ans != float('inf') else -1
            
            
        

#attempt4 : WA : Changed to array implementation and binary seaarch.
#Same index shouldn't be included
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        frontsum = [0]
        endsum = [0]
        for i in nums:
            frontsum.append(i+frontsum[-1])
        for i in nums[::-1]:
            endsum.append(i+endsum[-1])
        ans = float('inf')
        n = len(frontsum)
        
        def binsearch(key):
            low = 0
            end = n-1
            while(low<=end):
                mid = (low+end)//2
                if endsum[mid] == key:
                    return mid
                if endsum[mid] > key:
                    end = mid-1
                else:
                    low = mid+1
            return -1
        
        for index in range(n):
            if frontsum[index] <= x:
                endindex = binsearch(x-frontsum[index])
                if endindex != -1:
                    ans = min(ans,index+endindex)
        
        return ans if ans != float('inf') else -1
'''

#attempt2&3: Memory Error because of 10^19 stuff
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        @lru_cache(None)
        def finditerations(value,nums_start_index,nums_end_index):
            if value == 0:
                return 0
            if nums_start_index > nums_end_index:
                return float('inf')
            ans = float('inf')
            if nums[nums_start_index] <= value:
                ans = min(ans,1+finditerations(value-nums[nums_start_index],nums_start_index+1,nums_end_index))
            if nums[nums_end_index] <= value:
                ans = min(ans,1+finditerations(value-nums[nums_end_index],nums_start_index,nums_end_index-1))
            return ans
        
        ans = finditerations(x,0,len(nums)-1)
        return ans if ans != float('inf') else -1
'''

#attempt1: WA because you need to first find because we need to check value first
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        @lru_cache(None)
        def finditerations(value,nums_start_index,nums_end_index):
            if nums_start_index > nums_end_index:
                return float('inf')
            if value == 0:
                return 0
            ans = float('inf')
            if nums[nums_start_index] <= value:
                ans = min(ans,1+finditerations(value-nums[nums_start_index],nums_start_index+1,nums_end_index))
            if nums[nums_end_index] <= value:
                ans = min(ans,1+finditerations(value-nums[nums_end_index],nums_start_index,nums_end_index-1))
            return ans
        
        ans = finditerations(x,0,len(nums)-1)
        return ans if ans != float('inf') else -1
'''
