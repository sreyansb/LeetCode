#attempt2:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        di = {}
        curlen = 0
        start = 0
        maxlen = 0
        for index in range(len(s)):
            char = s[index]
            if char in di:
                start_copy = di[char]+1
                for character_to_be_removed in s[start:di[char]+1]:
                    curlen -= 1
                    del di[character_to_be_removed]
                start = start_copy
            di[char] = index
            curlen += 1
            maxlen = max(maxlen,curlen)
        return maxlen
            
#attempt1: WA becuase new strings should start from 1+old position of character
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        di = {}
        curlen = 0
        start = 0
        maxlen = 0
        for index in range(len(s)):
            char = s[index]
            if char in di:
                for character_to_be_removed in s[start:index]:
                    curlen -= 1
                    del di[character_to_be_removed]
                start = index
            di[char] = index
            curlen += 1
            maxlen = max(maxlen,curlen)
        return maxlen
            
        
'''
