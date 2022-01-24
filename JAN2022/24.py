#attempt2:
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())
        

#attempt1: WA didn't read the question properly
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper()
        
'''
