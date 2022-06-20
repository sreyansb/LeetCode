#attempt1:
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = {}
        
        for word in words:
            k = trie
            for char in word[::-1]:
                if char not in k:
                    k[char] = {}
                k = k[char]
            k["#"] = True
            
        def recurse(trie,currentlevel = 0):
            #print(trie)
            if len(trie) == 1 and '#' in trie:
                return 1
            ans = 0
            count = 0
            for char in trie:
                if char == "#":
                    continue
                count += 1
                ans += 1+recurse(trie[char],currentlevel+1)
            return ans + (count-1)*currentlevel
        
        return recurse(trie)
                
            
            
        
