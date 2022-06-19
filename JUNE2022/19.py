#attempt2:
from sortedcontainers import SortedList
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {}
        for word in products:
            k = trie
            for char in word:
                if char not in k:
                    k[char] = {}
                k = k[char]
                if "words" not in k:
                    k["words"] = SortedList()
                k["words"].add(word)
        ans = []
        n = len(searchWord)
        k = trie
        for char in searchWord:
            if char not in k:
                break
            k = k[char]
            ans.append(k["words"][:3])
        for i in range(n-len(ans)):
            ans.append([])
        return ans

#attempt1:WA
'''
from sortedcontainers import SortedList
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {}
        for word in products:
            k = trie
            for char in word:
                if char not in k:
                    k[char] = {}
                k = k[char]
                if "words" not in k:
                    k["words"] = SortedList()
                k["words"].add(word)
        ans = []
        n = len(searchWord)
        k = trie
        for char in searchWord:
            if char not in k:
                break
            k = k[char]
            ans.append(k["words"][:3])
        ans += []*(n-len(ans)) #this line doesn't work as expected
        return ans
'''
