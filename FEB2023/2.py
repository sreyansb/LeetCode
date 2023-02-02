#attempt1: TOOK HELP
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        di = {}
        for index, char in enumerate(order):
            di[char] = index
        def checkWord(word):
            return [di[char] for char in word]
        return words == sorted(words,key= lambda x: checkWord(x))
        
