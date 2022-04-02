#attempt2: 1500ms
class Solution:
    def validPalindrome(self, s: str) -> bool:
        @lru_cache(None)
        def check(low,high,is_cancelled_before):
            if low>=high:
                return True
            if s[low] == s[high]:
                return check(low+1,high-1,is_cancelled_before)
            else:
                if is_cancelled_before:
                    return False
                return check(low+1,high,True) or check(low,high-1,True)
        return check(0,len(s)-1,False)
        

#attempt1: 424ms
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(low,high,is_cancelled_before):
            if low>=high:
                return True
            if s[low] == s[high]:
                return check(low+1,high-1,is_cancelled_before)
            else:
                if is_cancelled_before:
                    return False
                return check(low+1,high,True) or check(low,high-1,True)
        return check(0,len(s)-1,False)
        
