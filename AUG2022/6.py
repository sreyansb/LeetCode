#attempt2:
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        tests = (minutesToTest//minutesToDie)+1
        ans = 1
        testcopy = tests
        while(tests<buckets):
            tests *= testcopy
            ans += 1
        return ans
            
        
        

#attempt1: WA
'''
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests = (minutesToTest//minutesToDie)+1
        ans = 1
        testcopy = tests
        while(tests<buckets):
            tests *= testcopy
            ans += 1
        return ans
'''
