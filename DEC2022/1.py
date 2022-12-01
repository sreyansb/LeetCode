#attempt1:
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        def countVowels(word):
            return len([i for i in word if i in "aeiou"])
        return countVowels(s[:n//2]) == countVowels(s[n//2:])
