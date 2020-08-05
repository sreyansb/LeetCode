def helper(root,word):
    if word=="" and '$' in root:
        return True
    if word=="" and '$' not in root:
        return False
    if word[0] in root:
        return helper(root[word[0]],word[1:])
    else:
        if word[0]!='.':
            return False
        else:
            ans=False
            for i in root:
                if i!='$':
                    ans|=helper(root[i],word[1:])
                if ans:
                    break
            return ans
class WordDictionary:
    
    def __init__(self):
        self.root={}      

    def addWord(self, word: str) -> None:
        root=self.root
        for i in word:
            if i not in root:
                root[i]={}
            root=root[i]
        root['$']=1
                
    def search(self, word: str) -> bool:
        root=self.root
        return helper(root,word)
                
# Your WordDictionary object will be instantiated and called as such:
word='a'
obj = WordDictionary()
obj.addWord(word)
print(obj.root)
obj.addWord(word)
print(obj.root)
print(obj.search(word))
