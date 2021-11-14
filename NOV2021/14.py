#attempt2:
def count1s(n):
        c = 0
        while(n):
            c += n&1
            n >>= 1
        return c
class CombinationIterator:
    
    def __init__(self, characters: str, combinationLength: int):
        self.chararr = sorted(set(characters))
        self.len = len(self.chararr)
        self.allowed = []
        self.index = 0
        for i in range(1<<self.len):
            if count1s(i) == combinationLength:
                word = bin(i)[2:]
                self.allowed.append("0"*(self.len-len(word))+word)
        print(self.chararr,self.allowed)
        self.hasnext = len(self.allowed)
            
    def next(self) -> str:
        if self.index < self.hasnext:
            self.index += 1
            #print([self.chararr[i] for i in range(self.len) if self.allowed[self.index-1][i] == "1"])
            word = "".join([self.chararr[i] for i in range(self.len) if self.allowed[self.hasnext-(self.index-1)-1][i] == "1"])
            #print(word)
            return word
        
    
    def hasNext(self) -> bool:
        return self.index < self.hasnext
        
# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

#attempt1: WA : because Didn't think through, cant reverse the sort
#because self.chararr wont map to larger numbers
'''
def count1s(n):
        c = 0
        while(n):
            c += n&1
            n >>= 1
        return c
class CombinationIterator:
    
    def __init__(self, characters: str, combinationLength: int):
        self.chararr = sorted(set(characters),reverse=True)
        self.len = len(self.chararr)
        self.allowed = []
        self.index = 0
        for i in range(1<<self.len):
            if count1s(i) == combinationLength:
                word = bin(i)[2:]
                self.allowed.append("0"*(self.len-len(word))+word)
        self.hasnext = len(self.allowed)
            
    def next(self) -> str:
        if self.index < self.hasnext:
            self.index += 1
            #print([self.chararr[i] for i in range(self.len) if self.allowed[self.index-1][i] == "1"])
            word = "".join([self.chararr[i] for i in range(self.len-1,-1,-1) if self.allowed[self.index-1][i] == "1"])
            #print(word)
            return word
        
    
    def hasNext(self) -> bool:
        return self.index < self.hasnext
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
'''