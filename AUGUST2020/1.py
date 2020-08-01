#3rd attempt
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or (ord(word[0])>64 and word[1:].islower()) :
            return True
        else:
            return False
        

#2nd attempt
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()) :
            return True
        else:
            return False
        
"""

#1st attempt
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
"""      
