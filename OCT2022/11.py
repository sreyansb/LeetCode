#attempt4: TOOK HELP
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<3:
            return False
        minsToTheLeft = [nums[0]]*n
        maxsToTheRight = [nums[-1]]*n
        for index in range(1,n):
            minsToTheLeft[index] = min(minsToTheLeft[index-1],nums[index])
        for index in range(n-2,-1,-1):
            maxsToTheRight[index] = max(maxsToTheRight[index+1],nums[index])
        for index in range(1,n-1):
            if minsToTheLeft[index] < nums[index] < maxsToTheRight[index]:
                return True
        return False

#attempt3: Very bad soln
from sortedcontainers import SortedList
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        di = {}
        maxele = -float('inf')
        sortedList = SortedList([])
        lenOfList = 0
        for ele in nums[::-1]:
            if ele in di:
                sortedList.remove(ele)
                lenOfList -= 1
            sortedList.add(ele)
            lenOfList += 1
            pos = sortedList.index(ele)
            if pos != lenOfList-1:
                di[ele] = True
                if di[sortedList[pos+1]]:
                    return True
            else:
                di[ele] = False
        return False
            
                

#attempt2: WA
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        index = n-1
        s = set()
        nums.reverse()
        while(index > -1 and len(s) != 2):
            s.add(nums[index])
            index -= 1
        if index == -1:
            return False
        min1 = min(s)
        min2 = sum(s) - min1
        while(index >= 0):
            if nums[index] > min2:
                return True
            if nums[index] < min1:
                min2 = min1
                min1 = nums[index]
            elif nums[index] < min2:
                min2 = nums[index]
            index -= 1
        return False
'''

#attempt1: WA
'''
from sortedcontainers import SortedList
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        a = SortedList([nums[-1],nums[-2]])
        cur_length = 2
        for number in range(n-3,-1,-1):
            pos = a.bisect_right(nums[number])
            if pos <= cur_length-2:
                return True
            a.add(nums[number])
            cur_length += 1
        return False
'''
