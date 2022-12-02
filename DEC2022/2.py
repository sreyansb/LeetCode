#attempt3:
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return sorted(list(Counter(word1).values())) == sorted(list(Counter(word2).values()))
and sorted(list(Counter(word1).keys())) == sorted(list(Counter(word2).keys()))

#attempt2: WA because didn't check the keys WHAT AN IDIOT
'''
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return sorted(list(Counter(word1).values())) == sorted(list(Counter(word2).values()))
'''

#attempt1: WA because didn't sort the list
'''
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return list(Counter(word1).values()) == list(Counter(word2).values())
'''
