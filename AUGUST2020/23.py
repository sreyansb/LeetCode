#ATTEMPT-3 NOT A TLE, worked well enough.Use a reversed Trie
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie={}
        for i in words:
            k=self.trie
            j=i[::-1]
            for f in j:
                if f not in k:
                    k[f]={}
                k=k[f]
            k['$']=1
        print(self.trie)
        self.past=""

    def query(self, letter: str) -> bool:
        self.past+=letter
        ans=True
        k=self.trie
        for i in self.past[::-1]:
            if i not in k:
                ans=False
                break
            k=k[i]
            if '$' in k:
                break
        if ans and '$' in k:
            return True
        return False
"""
#Attempt 2: Changed implementation from tries to lists but still slow
class StreamChecker:

    def __init__(self, words: List[str]):
        self.li=[[] for i in range(26)]
        for i in words:
            self.li[ord(i[-1])-97].append(i)
        self.past=""
        
    def query(self, letter: str) -> bool:
        self.past+=letter
        k = self.li[ord(letter)-97]
        if not(k):
            return False
        for i in range(len(self.past)-1,-1,-1):
            if self.past[i:] in k:
                return True
        return False
            
"""

"""
Attempt 1: Used tries
class StreamChecker:

    def __init__(self, words: List[str]):
        self.di={}
        for i in words:
            k=self.di
            for j in i:
                if j not in k:
                    k[j]={}
                k=k[j]
            k['$']=1
        self.past=[]

    def query(self, letter: str) -> bool:
        self.past.append(letter)
        for i in range(len(self.past)-1,-1,-1):
            k=self.di
            ans=True
            for j in range(i,len(self.past)):
                if self.past[j] not in k:
                    ans=False
                    break
                k=k[self.past[j]]
            if ans==True and '$' in k:
                return True
        return False

"""

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
