#attempt2:
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            k = trie
            for char in word:
                if char not in k:
                    k[char] = {}
                k = k[char]
            if '#' not in k:
                k['#'] = 0
            k['#'] += 1
        ans = []
        def findWord(word,wordLen,index,curTrie,noOfWords=0):
            if index >= wordLen:
                ansHere = '#' in curTrie and noOfWords>0
                return ansHere
            if word[index] not in curTrie:
                return False
            curTrie = curTrie[word[index]]
            if '#' in curTrie:
                return findWord(word,wordLen,index+1,curTrie,noOfWords) or findWord(word,wordLen,index+1,trie,noOfWords+1)
            return findWord(word,wordLen,index+1,curTrie,noOfWords)
        for word in words:
            if findWord(word,len(word),0,trie):
                ans.append(word)
        return ans
        
            

#attempt1:
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            k = trie
            for char in word:
                if char not in k:
                    k[char] = {}
                k = k[char]
            if '#' not in k:
                k['#'] = 0
            k['#'] += 1
        ans = []
        def findWord(word,index,curTrie,noOfWords=0):
            if index >= len(word):
                ansHere = '#' in curTrie and noOfWords>0
                return ansHere
            if word[index] not in curTrie:
                return False
            curTrie = curTrie[word[index]]
            if '#' in curTrie:
                return findWord(word,index+1,curTrie,noOfWords) or findWord(word,index+1,trie,noOfWords+1)
            return findWord(word,index+1,curTrie,noOfWords)
        for word in words:
            if findWord(word,0,trie):
                ans.append(word)
        return ans
        
            
