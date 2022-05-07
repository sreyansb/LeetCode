from sortedcontainers import SortedList
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        left_lesser = SortedList([])
        right_lesser = SortedList([])
        n = len(nums)
        lesser_cond = [(False,-1)]*n
        left_lesser.add(nums[0])
        for index in range(1,n):
            i = nums[index]
            pos = left_lesser.bisect_left(i)
            if pos != 0:
                lesser_cond[index] = (True,left_lesser[0])
            left_lesser.add(i)
        ans = False
        right_lesser.add(nums[-1])
        for index in range(n-2,-1,-1):
            i = nums[index]
            if lesser_cond[index][0]:
                pos = right_lesser.bisect_left(i)
                if pos != 0:
                    if right_lesser[pos-1] > lesser_cond[index][1]:
                        ans = True
                        break
            right_lesser.add(i)
        #print(lesser_cond)
        return ans
                
                
        
