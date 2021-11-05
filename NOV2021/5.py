#attempt2: 40ms
class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 1
        end = 100000
        ans = -1
        while(start<=end):
            mid = (start+end)//2
            required = (mid*(mid+1))//2
            if required == n:
                return mid
            if required>n:
                end = mid-1
            else:
                ans = mid
                start = mid+1
        return ans

#attempt1: 1320ms
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        steps = 1
        completerows = 0
        while(n):
            if n<steps:
                break
            completerows += 1
            n -= steps
            steps += 1
        return completerows
'''
