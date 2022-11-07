#attempt1:
class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        leftMostSixIndex = s.find('6')
        if leftMostSixIndex != -1:
            return int(s[:leftMostSixIndex]+'9'+s[leftMostSixIndex+1:])
        return num
