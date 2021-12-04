#attempt3: AC : use a trie such that the end of a word is the root of the word
#then for each word, use that
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.curword = ""
        for i in words:
            k = self.trie
            for j in i[::-1]:
                if j not in k:
                    k[j] = {}
                k = k[j]
            k['#'] = 1
        #print(self.trie)
    def query(self, letter: str) -> bool:
        self.curword += letter
        k = self.trie
        for i in self.curword[::-1]:
            if i not in k:
                return False
            k = k[i]
            if '#' in k:
                return True
        return False

#attempt2: WA : Silly mistake didn't do k = k[j] if when j in k
'''
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.curword = ""
        for i in words:
            k = self.trie
            for j in i[::-1]:
                if j not in k:
                    k[j] = {}
                    k = k[j]
            k['#'] = 1
        
    def query(self, letter: str) -> bool:
        self.curword += letter
        k = self.trie
        for i in self.curword[::-1]:
            if i not in k:
                return False
            k = k[i]
            if '#' in k:
                return True
        return False
'''

#attempt1: TLE basic code brute force
'''
class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = set(words)
        self.curword = ""
        self.leng = 0
        
    def query(self, letter: str) -> bool:
        self.curword += letter
        self.leng += 1
        for i in range(self.leng):
                if self.curword[i:] in self.words:
                    return True
        return False
'''
