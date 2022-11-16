#attempt1:
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while (low <= high):
            mid = (low+high)//2
            guessMid = guess(mid)
            if guessMid == -1:
                high = mid-1
            elif guessMid == 1:
                low = mid+1
            else:
                return mid
        return -1
        
