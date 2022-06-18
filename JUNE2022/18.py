#attempt2: TOOK HINT
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {}
        
        def insert_into_trie(word,index):
            k = self.trie
            for char in word:
                if char not in k:
                    k[char] = {}
                k = k[char]
                k["index"] = index
            k["index"] = index
                
        for index,word in enumerate(words):
            for word_index in range(len(word)):
                insert_into_trie(word[word_index:]+"#"+word,index)

    def f(self, prefix: str, suffix: str) -> int:
        k = self.trie
        word = suffix + "#" + prefix
        for char in word:
            if char not in k:
                return -1
            k = k[char]
        return k["index"]
        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

#attempt1: TLE
'''
class WordFilter:

    def __init__(self, words: List[str]):
        self.prefixtrie = {}
        self.suffixtrie = {}
        self.prefixtrie["allowed_indices"] = set()
        self.suffixtrie["allowed_indices"] = set()
        for index,word in enumerate(words):
            k = self.prefixtrie
            k["allowed_indices"].add(index)
            for char in word:
                if char not in k:
                    k[char] = {}
                k = k[char]
                if "allowed_indices" not in k:
                    k["allowed_indices"] = set()
                k["allowed_indices"].add(index)
                
            j = self.suffixtrie
            j["allowed_indices"].add(index)
            for char in word[::-1]:
                if char not in j:
                    j[char] = {}
                j = j[char]
                if "allowed_indices" not in j:
                    j["allowed_indices"] = set()
                j["allowed_indices"].add(index)     
                
    def f(self, prefix: str, suffix: str) -> int:
        k = self.prefixtrie
        for char in prefix:
            if char not in k:
                return -1
            k = k[char]
        j = self.suffixtrie
        for char in suffix[::-1]:
            if char not in j:
                return -1
            j = j[char]
        ans_index = k["allowed_indices"]&j["allowed_indices"]
        if ans_index:
            return max(ans_index)
        return -1
            
            
            
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
'''
