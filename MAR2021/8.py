#attempt1: Took Hint: Max number is 2-remove all a's first followed by all b's
#if initially it is palindrome: 1 step required
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if s==s[::-1]:
            return 1
        return 2
        
