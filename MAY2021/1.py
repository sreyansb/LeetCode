#attempt3: AC using tries
class WordFilter:
    def __init__(self, words: List[str]):
        self.trie={}
        
        def insertintotrie(trie,string,index):
            for i in string:
                if i not in trie:
                    trie[i]={}
                    trie[i]["i"]=index
                trie[i]["i"]=index
                trie=trie[i]
        
        for i in range(len(words)):
            curstr=""
            insertintotrie(self.trie,curstr+"#"+words[i],i)
            for j in words[i][::-1]:
                curstr=curstr+j
                insertintotrie(self.trie,curstr+"#"+words[i],i)
        #print(self.trie)
        

    def f(self, prefix: str, suffix: str) -> int:
        def searchintrie(trie,word):
            for i in word:
                if not (trie[i]):
                    return -1
                trie=trie[i]
            return trie["i"]
        word=suffix[::-1]+"#"+prefix
        return searchintrie(self.trie,word)

#attempt2:TLE as expected
'''
class WordFilter:

    def __init__(self, words: List[str]):
        self.list=[]
        for i in range(len(words)):
            curstr=""
            self.list.append((curstr+"#"+words[i],i))
            for j in words[i][::-1]:
                curstr=curstr+j
                self.list.append((curstr+"#"+words[i],i))
        self.list=self.list[::-1]
        #print(self.list)

    def f(self, prefix: str, suffix: str) -> int:
        word=suffix[::-1]+"#"+prefix
        #print(word)
        for i in self.list:
            if word in i[0]:
                return i[1]
    
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
'''

#attempt1: WA didn't reverse word while searching in self.list
#MAIN IDEA: for every suffix of a word put into self.list
#a word of the form suffix#fullword
'''
class WordFilter:

    def __init__(self, words: List[str]):
        self.list=[]
        for i in range(len(words)):
            curstr=""
            self.list.append((curstr+"#"+words[i],i))
            for j in words[i][::-1]:
                curstr=curstr+j
                self.list.append((curstr+"#"+words[i],i))
        self.list=self.list[::-1]

    def f(self, prefix: str, suffix: str) -> int:
        word=suffix+"#"+prefix
        print(word)
        for i in self.list:
            if word in i[0]:
                return i[1]
                    
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
'''
