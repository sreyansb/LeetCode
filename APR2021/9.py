#attempt1:
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        di={}
        for i in range(26):
            di[order[i]]=i
        def fn(word):
            return [di[x] for x in word]
        sa=sorted(words,key=lambda x:fn(x))
        return sa==words
        
        
