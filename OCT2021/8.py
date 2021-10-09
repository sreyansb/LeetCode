#attempt1: 94%

class Trie:

    def __init__(self):
        self.trie={}        

    def insert(self, word: str) -> None:
        k=self.trie
        for i in word:
            if i not in k:
                k[i]={}
            k=k[i]
        k["#"]=1

    def search(self, word: str) -> bool:
        k=self.trie
        for i in word:
            if i not in k:
                return False
            k=k[i]
        return "#" in k

    def startsWith(self, prefix: str) -> bool:
        k=self.trie
        for i in prefix:
            if i not in k:
                return False
            k=k[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
