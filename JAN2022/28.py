#attempt1:
class WordDictionary:

    def __init__(self):
        self.trie = {}        

    def addWord(self, word: str) -> None:
        k = self.trie
        for i in word:
            if i not in k:
                k[i] = {}
            k = k[i]
        k['$'] = True        

    def search(self, word: str) -> bool:
        def recursive(curdi,curstr):
            if not(curdi):
                return False
            if not(curstr):
                if '$' in curdi:
                    return True
                return False
            if curstr[0] == ".":
                ans = False
                for i in curdi:
                    if i!="$":
                        ans = recursive(curdi[i],curstr[1:])
                        if ans:
                            break
                return ans
            else:
                if curstr[0] not in curdi:
                    return False
                return recursive(curdi[curstr[0]],curstr[1:])
        return recursive(self.trie,word)
                        
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
