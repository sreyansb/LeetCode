#attempt2:
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        start = 0
        end = n-1
        while(start<end):
            if palindrome[start] != 'a':
                return palindrome[:start] + "a" + palindrome[start+1:]
            start += 1
            end -= 1
        return palindrome[:n-1]+"b"
        
#attempt1: WA because didn't take care of palindrome strings of odd lengths
'''
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        start = 0
        end = n-1
        while(start<=end):
            if palindrome[start] != 'a':
                return palindrome[:start] + "a" + palindrome[start+1:]
            start += 1
            end -= 1
        return palindrome[:n-1]+"b"
        
'''
