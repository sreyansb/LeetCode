#attempt7:
from sortedcontainers import SortedList
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        minDiff = float('inf')
        answer = float('inf')
        nums.sort()
        for index in range(n):
            start = index + 1
            end = n - 1
            while(start < end):
                valToCheck = nums[index]+nums[start]+nums[end]
                if nums[index]+nums[start]+nums[end] > target:
                    end -= 1
                else:
                    start += 1
                val = abs(target-valToCheck)
                if minDiff > val:
                    minDiff = val
                    answer = valToCheck
            if minDiff == 0:
                break
        return answer
                    
            

#attempt 3,4,5,6: TOOK HRLP: COPIED TLE
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        mindiff=float('inf')
        sumatdiff=float('inf')
        nums.sort()
        for i in range(n):
            start=i+1
            end=n-1
            while(start<end):
                if nums[i]+nums[start]+nums[end]<target:
                    if mindiff>abs(nums[i]+nums[start]+nums[end]-target):
                        mindiff=abs(nums[i]+nums[start]+nums[end]-target)
                        sumatdiff=nums[i]+nums[start]+nums[end]
                    start+=1
                else:
                    if mindiff>abs(nums[i]+nums[start]+nums[end]-target):
                        mindiff=abs(nums[i]+nums[start]+nums[end]-target)
                        sumatdiff=nums[i]+nums[start]+nums[end]
                    end-=1
        return sumatdiff
                    
        
'''

#attempt2: WA
'''
from sortedcontainers import SortedList
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        minDiff = float('inf')
        answer = float('inf')
        for index in range(n):
            #nums[index]]
            seenNumbers = SortedList()
            len_seen = 0
            for nextIndex in range(index+1,n):
                #number to find is target-nums[index]-nums[nextIndex]
                if len_seen == 0:
                    seenNumbers.add(nums[nextIndex])
                    len_seen += 1
                    continue
                posLeft = seenNumbers.bisect_left(target-nums[index]-nums[nextIndex])
                posRight = seenNumbers.bisect_right(target-nums[index]-nums[nextIndex])
                if posLeft == len_seen:
                    posLeft = 0
                if posRight == len_seen:
                    posRight = 0
                curDiff = abs(target - nums[index]-nums[nextIndex]-seenNumbers[posLeft])
                if minDiff > curDiff:
                    minDiff = curDiff
                    answer = nums[index]+nums[nextIndex]+seenNumbers[posLeft]
                curDiff = abs(target - nums[index]-nums[nextIndex]-seenNumbers[posRight])
                if minDiff > curDiff:
                        minDiff = curDiff
                        answer = nums[index]+nums[nextIndex]+seenNumbers[posRight]
                seenNumbers.add(nums[nextIndex])
                len_seen += 1
        return answer 
                    
'''

#attempt1: WA some bad idea
'''
from sortedcontainers import SortedList
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        minDiff = float('inf')
        answer = float('inf')
        for index in range(n):
            seen_numbers = SortedList()
            len_of_seen = 0
            for nextIndex in range(index+1,n):
                #find a number closest to target - nums[index] - nums[nextIndex]
                #|target-(nums[index]+nums[nextIndex]+nums[thirdIndex])| should be close to 0
                pos = seen_numbers.bisect_left(target - nums[index] - nums[nextIndex])
                if pos != len_of_seen:
                    curDiff = abs(target - nums[index] - nums[nextIndex]-seen_numbers[pos])
                    if minDiff > curDiff:
                        minDiff = curDiff
                        answer = nums[index] + nums[nextIndex] + seen_numbers[pos]
                seen_numbers.add(nums[nextIndex])
                #print(nextIndex,index,pos,seen_numbers)
                len_of_seen += 1
            seen_numbers = SortedList()
            len_of_seen = 0
            for nextindex in range(index+1,n):
                #find a number closest to target - nums[index] - nums[nextIndex]
                #|target-(nums[index]+nums[nextIndex]+nums[thirdIndex])| should be close to 0
                pos = seen_numbers.bisect_right(target - nums[index] - nums[nextIndex])
                if pos != 0:
                    curDiff = abs(target - nums[index] - nums[nextIndex]-seen_numbers[pos-1])
                    if minDiff > curDiff:
                        minDiff = curDiff
                        answer = nums[index] + nums[nextIndex] + seen_numbers[pos-1]
                seen_numbers.add(nums[nextIndex])
                len_of_seen += 1
        return answer
'''
